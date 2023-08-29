# QnA Bestie on PDF

The app takes a PDF and allows user to ask questions and provides corresponding answers extracted from PDFs. The AI behind the app is the Llama2 model. While the model is open source and offers free usage, the challenge lies in the computationally expensive setup, therefore in this project replicate API has been used which has a free API quota. Upload your file and get your answers today!

## Features

- Upload a PDF file.
- Ask questions about the PDF content.
- Obtain answers using the Llama2 AI model.

## Getting Started

Follow these steps to set up and run the PDF Question-Answering App on your local machine.

### Installation

1. Clone the repository or download the ZIP file.

   ```bash
   git clone https://github.com/rohancode/QnA-Bestie-On-PDF.git

2. Navigate to the project directory:

   ```bash
   cd QnA-Bestie-On-PDF

3. Install required Python packages using pip:

   ```bash
   pip install -r requirements.txt

4. Add the content to the `.env` file:
   ```dotenv
   PINECODE_API_TOKEN="PINECODE_API_TOKEN"
   PINECONE_ENV="PINECONE_ENV"
   PINECONE_INDEX="PINECONE_INDEX"
   REPLICATE_API_TOKEN="REPLICATE_API_TOKEN"
   REPLICATE_MODEL_ENDPOINT13B=a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5

### Usage

1. Run the app

   ```bash
   streamlit run app.py

2. Access the app through your web browser by visiting `http://localhost:8501`

3. Upload a PDF file

4. Input your questions

### Demo

![Demo](https://github.com/rohancode/.../abc.gif)

## Contact

If you have any questions or suggestions, please feel free to open an issue or contact me at rohan.rathore93@gmail.com.