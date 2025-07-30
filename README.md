\# Adobe Hackathon – Round 1A: PDF Outline Extractor



\##  Objective



Extract a structured outline from PDF documents, including:

\- Title (from PDF metadata or fallback to filename)

\- Headings classified into H1, H2, H3 (based on font size)

\- Page numbers of headings



The program runs completely offline, on CPU, inside a Docker container.



---



\## Folder Structure



pdf\_outline\_extractor11/

├── app/

│ ├── main.py

│ ├── utils.py

│ └── requirements.txt

├── input/ 

│ └── sample.pdf

├── output/ 

├── Dockerfile

└── README.md

