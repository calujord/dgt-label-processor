# DGT Label Processor

Este proyecto permite procesar números de matrícula para obtener la etiqueta ambiental de la DGT (Dirección General de Tráfico) en España.

## Requisitos

- Python 3.7 o superior
- `requests`
- `beautifulsoup4`

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/calujord/dgt-label-processor.git
    cd dgt-label-processor
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el script y obtener la etiqueta de una matrícula, usa el siguiente comando:

```sh
python main.py 1234-ABC