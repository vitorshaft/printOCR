# Ferramenta de Captura de Tela com OCR

## Descrição

Uma ferramenta de captura de tela que permite ao usuário selecionar uma área da tela para captura e, em seguida, realiza o OCR (Reconhecimento Óptico de Caracteres) na imagem capturada. Após a captura e reconhecimento do texto, o texto é exibido em uma janela auxiliar com duas opções: salvar o texto na área de transferência ou tentar a captura novamente.

## Funcionalidades

- Captura de uma área da tela selecionada pelo usuário.
- Reconhecimento de texto na imagem capturada usando OCR.
- Exibição do texto reconhecido em uma janela auxiliar.
- Opção para salvar o texto na área de transferência.
- Opção para tentar a captura novamente.

## Requisitos

- Python 3.9 ou superior
- Pillow
- PyQt5
- pytesseract
- Tesseract-OCR

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/vitorshaft/printOCR.git
    cd printOCR
    ```

2. Instale as dependências:
    ```sh
    pip install Pillow PyQt5 pytesseract
    ```

3. Instale o Tesseract-OCR:
    - Windows: Baixe e instale [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
    - Linux:
        ```sh
        sudo apt-get install tesseract-ocr
        ```

4. Configure o caminho do Tesseract nas variáveis de ambiente:
    - Windows:
        1. Adicione o caminho do executável do Tesseract (por exemplo, `C:\Program Files\Tesseract-OCR`) às variáveis de ambiente do sistema.
        2. Adicione a variável de ambiente `TESSDATA_PREFIX` com o valor `C:\Program Files\Tesseract-OCR\tessdata`.

    - Linux:
        1. Adicione o caminho do executável do Tesseract ao `PATH`:
            ```sh
            export PATH=$PATH:/usr/local/bin/tesseract
            ```
        2. Adicione a variável de ambiente `TESSDATA_PREFIX`:
            ```sh
            export TESSDATA_PREFIX=/usr/local/share/tessdata
            ```

## Uso

1. Execute o script Python:
    ```sh
    python printOCR.py
    ```

2. Selecione a área da tela que deseja capturar.
3. Após a captura, o texto reconhecido será exibido em uma janela auxiliar.
4. Use os botões para salvar o texto na área de transferência ou tentar a captura novamente.

---

# Screen Capture Tool with OCR

## Description

A screen capture tool that allows the user to select an area of the screen for capture and then performs OCR (Optical Character Recognition) on the captured image. After capturing and recognizing the text, the text is displayed in an auxiliary window with two options: save the text to the clipboard or retry the capture.

## Features

- Capture an area of the screen selected by the user.
- Text recognition in the captured image using OCR.
- Display the recognized text in an auxiliary window.
- Option to save the text to the clipboard.
- Option to retry the capture.

## Requirements

- Python 3.9 or higher
- Pillow
- PyQt5
- pytesseract
- Tesseract-OCR

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/vitorshaft/printOCR.git
    cd printOCR
    ```

2. Install the dependencies:
    ```sh
    pip install Pillow PyQt5 pytesseract
    ```

3. Install Tesseract-OCR:
    - Windows: Download and install [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
    - Linux:
        ```sh
        sudo apt-get install tesseract-ocr
        ```

4. Set up Tesseract in environment variables:
    - Windows:
        1. Add the path to the Tesseract executable (e.g., `C:\Program Files\Tesseract-OCR`) to the system environment variables.
        2. Add the environment variable `TESSDATA_PREFIX` with the value `C:\Program Files\Tesseract-OCR\tessdata`.

    - Linux:
        1. Add the path to the Tesseract executable to the `PATH`:
            ```sh
            export PATH=$PATH:/usr/local/bin/tesseract
            ```
        2. Add the environment variable `TESSDATA_PREFIX`:
            ```sh
            export TESSDATA_PREFIX=/usr/local/share/tessdata
            ```

## Usage

1. Run the Python script:
    ```sh
    python printOCR.py
    ```

2. Select the area of the screen you want to capture.
3. After capturing, the recognized text will be displayed in an auxiliary window.
4. Use the buttons to save the text to the clipboard or retry the capture.
