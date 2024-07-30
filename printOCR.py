from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from PIL import ImageGrab
import pytesseract
import clipboard

class ScreenCapture(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Screen Capture Tool')
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setWindowOpacity(0.3)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('red'), 3))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.capture()
        self.close()

    def capture(self):
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(0, x1, y1, x2-x1, y2-y1)
        screenshot.save('screenshot.png', 'png')
        self.perform_ocr('screenshot.png')

    def perform_ocr(self, image_path):
        text = pytesseract.image_to_string(image_path)
        self.show_text_window(text)

    def show_text_window(self, text):
        self.text_window = TextWindow(text)
        self.text_window.show()

class TextWindow(QtWidgets.QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle('Captured Text')
        self.setGeometry(100, 100, 600, 400)
        self.layout = QtWidgets.QVBoxLayout()

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setPlainText(text)
        self.layout.addWidget(self.text_edit)

        self.button_layout = QtWidgets.QHBoxLayout()
        
        self.save_button = QtWidgets.QPushButton('Save to Clipboard', self)
        self.save_button.clicked.connect(self.save_to_clipboard)
        self.button_layout.addWidget(self.save_button)
        
        self.retry_button = QtWidgets.QPushButton('Retry Capture', self)
        self.retry_button.clicked.connect(self.retry_capture)
        self.button_layout.addWidget(self.retry_button)

        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def save_to_clipboard(self):
        clipboard.copy(self.text_edit.toPlainText())

    def retry_capture(self):
        self.close()
        self.capture_window = ScreenCapture()
        self.capture_window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ScreenCapture()
    window.show()
    sys.exit(app.exec_())
