# 🤖 AI Assignment Grading Assistant

An AI-powered web application that automatically evaluates student answers by comparing them with a reference (teacher) answer using Natural Language Processing (NLP) techniques. The system provides fair grading, partial marks, and meaningful feedback, reducing manual effort and improving consistency in evaluation.

---

## Problem Statement

Manual grading of subjective answers is time-consuming and often inconsistent. This project automates the grading process by:

* Analyzing student responses
* Comparing them against model answers
* Awarding marks based on concept coverage and semantic similarity
* Generating actionable feedback

This project aligns with the AI Assignment Grading Assistant problem statement and focuses on rubric-based evaluation and feedback generation.

---

## Features

* AI-based evaluation using NLP and text similarity
* Partial and full marking system
* Case-insensitive and variable-insensitive grading
* Allows extra relevant points without penalty
* Assigns zero marks for irrelevant answers
* Displays missing concepts required for full marks
* Modern, professional UI with color-coded results
* Green indicates excellent performance
* Yellow indicates average performance
* Red indicates poor performance
* Web-based interface built using Flask

---

## Tech Stack

Frontend:

* HTML5
* CSS3 (modern UI with gradients and cards)
* Google Fonts (Poppins)

Backend:

* Python
* Flask

AI / NLP:

* Scikit-learn
* TF-IDF vectorization
* Cosine similarity

---

## How It Works

User inputs:

* Student answer
* Reference (teacher) answer
* Maximum marks
* Rubrics

System processing:

* Normalizes text (case and variable insensitive)
* Calculates semantic similarity
* Checks concept coverage

Evaluation criteria:

* Concept coverage
* Semantic similarity

Output generated:

* Final score
* Performance remark
* Missing points (if any)
