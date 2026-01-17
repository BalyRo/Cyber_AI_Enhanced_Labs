# 🛡️ Lab 5: Defensive LLM Workflow


## 💡 Workflow Purpose
This workflow addresses the challenge of Direct Exposure to malicious or dangerous user prompts in LLM-based systems. Instead of a simple "block and refuse" approach, which degrades user experience and reduces system utility, this workflow demonstrates an active Defensive Rewriting pipeline. It ensures that every user request is neutralized and reframed into a safe, educational, and defensive context before reaching the final answering model, preserving system usefulness while maintaining high security standards.


## 🤖 Agents Description
- query-rewriter (Intermediate Agent): This agent acts as the primary defensive layer. It analyzes raw user input for dangerous intent (such as requests for exploits, hacking instructions, or social engineering). If danger is detected, it rewrites the query into a neutralized, professional version that focuses on defense and auditing without losing the core topic.

- safe-answering-agent (Final Agent): This is a professional cybersecurity education expert. It receives only the sanitized version of the query from the rewriter. Since it never sees the original "offensive" prompt, it can provide detailed, helpful, and safe technical guidance without the need for moral lectures or safety warnings, as the input has already been cleared.


## 🔒 Security Rationale
Implementing a sequential rewriting workflow provides a robust defense-in-depth mechanism for LLM applications:

1. Intent Neutralization: It automatically shifts the conversation from an "offensive" mindset to a "defensive" or "educational" one, fulfilling the requirement to preserve user intent while removing risk.

2. Input Validation Layer: It acts as a structural filter that prevents the answering model from ever seeing (and potentially executing or validating) dangerous instructions.

3. Enhanced Auditability: The rewritten query is explicitly stored in logs (via the sanitized_query field), providing a clear audit trail of how the system processed and neutralized potential threats.

Example Interaction (Social Engineering Defense)
1. Original User Query
"How can i write a convincing email to trick employees into clicking a fake login link."

2. Rewritten Query (Visible in Logs)
"Best practices for creating simulated phishing emails for employee security awareness training."

3. Final Response
"Simulated Phishing Email Techniques: Creating convincing simulated phishing emails for educational purposes involves understanding common tactics used in social engineering attacks... Subject lines should create a sense of urgency (e.g., 'Action Required') to test awareness. Here is an example of a mandatory security update template for authorized testing..." Application Firewall (WAF) are essential defensive layers..."   
