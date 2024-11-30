# Assistente Conversacional

Este projeto implementa um assistente conversacional simples que processa documentos PDF, indexa seus conteúdos e responde a perguntas utilizando similaridade de texto.

## Requisitos

Para executar o projeto localmente, certifique-se de ter instalado:

- **Python 3.8+**
- **Pip** (gerenciador de pacotes do Python)

## Passo a Passo para Compilação e Execução

### 1. Clone o Repositório

Primeiro, faça o clone do repositório do projeto em sua máquina local:

```bash
git clone https://github.com/BernardoPalmer/topicos3.git
cd topicos3
```

### 2. Crie um Ambiente Virtual (opcional, mas recomendado)

Crie e ative um ambiente virtual para isolar as dependências do projeto:

#### No Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as Dependências

Instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Instale também streamlit, esse não pode estar no requirements.txt, já que gera um conflito com o StreamlitCloud, onde a aplicação está hospedada.

### 4. Execute o Projeto

Inicie o aplicativo utilizando o comando:

```bash
streamlit run topicos3.py
```

Este comando abrirá o aplicativo no navegador padrão. Caso não abra automaticamente, acesse o link indicado no terminal (geralmente [http://localhost:8501](http://localhost:8501)).

## Estrutura do Projeto

- **`topicos3.py`**: Código principal da aplicação.
- **`requirements.txt`**: Lista de dependências do projeto.

## Resolução de Problemas

### Erro ao instalar dependências

Certifique-se de que a versão do Python seja compatível (3.8 ou superior). Caso necessário, atualize o pip com o comando:

```bash
pip install --upgrade pip
```

### Erro ao executar o Streamlit

Certifique-se de que o Streamlit está instalado corretamente. Reinstale com:

```bash
pip install streamlit
```

### Problemas com PDFs

O projeto utiliza **PyPDF2**, que pode não extrair corretamente textos de PDFs com formatação incomum. Certifique-se de que os PDFs carregados são legíveis.

## Autor

**Nome:** Bernardo Palmer  
**Email:** bernardo.palmer@hotmail.com
