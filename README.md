# Biometric Text Matcher
A simple simulation of biometric verification using string-based pattern comparison.

## Overview
This project compares two biometric-like text samples using **Levenshtein distance**, a metric that measures the similarity between sequences.  
It models how text-encoded biometric data (like DNA, voice signatures, or keys) could be compared.

## Features
- Text-based similarity measurement  
- Adjustable similarity threshold  
- Simple and lightweight code  
- Realistic for DNA or voice-key comparisons  

## Technologies Used
- **Python**
- **textdistance**

## Installation
```bash
pip install textdistance

## Usage
- Run main.py.
- The script compares two text samples and calculates similarity.
- Displays similarity percentage and whether verification succeeded.

## Project Structure
biometric_text_matcher/
├── main.py
├── verifier.py
├── requirements.txt
└── README.md

## Scalability
- Can evolve into:
- DNA-based biometric verification systems
- Text-based pattern matching APIs
- Voiceprint or speech pattern similarity checkers
