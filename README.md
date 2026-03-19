# LLM-Agent-RedTeam-Toolkit

An automated fuzzing framework and research substrate for evaluating Prompt Injection and Tool Hijacking vulnerabilities in agentic LLM deployments. 

This toolkit provides a controlled environment to identify, reproduce, and mitigate adversarial inputs that attempt to override instructional context or exfiltrate sensitive data. It includes a vulnerable target agent, an automated fuzzing engine, and a two-layer semantic guardrail architecture.

## Core Features

* **Attack Taxonomy Fuzzer:** Systematically executes four distinct attack vectors: Direct Override, Authority Impersonation, Diagnostic Privilege Escalation, and Indirect/Narrative Injection.
* **Empirical Target Agent:** Simulates an enterprise HR assistant powered by Llama 3.1-8B-Instant, built with the Groq API.
* **Semantic Guardrails:** Implements a pre-inference defensive layer combining Lexical Command Override Detection and Protected Entity Recognition.

## Installation & Setup

1. Clone the repository and navigate to the directory:
```bash
   git clone [https://github.com/yourusername/LLM-Agent-RedTeam-Toolkit.git](https://github.com/yourusername/LLM-Agent-RedTeam-Toolkit.git)
   cd LLM-Agent-RedTeam-Toolkit
```
2. Set up the virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Configure your API Key:
Create a .env file in the root directory and add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### Usage
1. Establish the Baseline Vulnerability
Run the fuzzer against the unprotected agent to observe data exfiltration across multiple vectors:
```bash
python fuzzer/fuzzer.py
```
2. Test the Defensive Architecture
Run the fuzzer against the secure agent to observe the semantic guardrails intercepting the payloads:

```bash
python fuzzer/fuzzer.py
```
### Research Paper
This toolkit serves as the empirical foundation for the paper: "Prompt Injection and Tool Hijacking in Agentic Large Language Model Systems: Attack Taxonomy, Empirical Evaluation, and Semantic Guardrail Design." Read the full paper in the /docs directory.

### License
MIT License. See LICENSE for details.

### Ethical Disclosure
All payloads and tools provided in this repository are intended strictly for educational purposes and authorized defensive research. Do not use these tools against systems you do not own or have explicit permission to test.
