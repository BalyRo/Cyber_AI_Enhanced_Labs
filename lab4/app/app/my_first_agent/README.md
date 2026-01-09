הנה גרסה קצרה וממוקדת ל-README.md עבור סוכן אבטחת המידע (security-agent), המבוססת על המבנה הטכני שביקשת:

🛡️ security-agent
1. Agent Name
security-agent

2. Agent Purpose
The purpose of this agent is to demonstrate automated security validation using specialized tools. It acts as a security assistant that evaluates user inputs (like passwords) against defined safety standards.

3. Agent Tools
3.1 check_password_length(password)
Purpose: Validates if a provided password string meets the minimum length requirement (8 characters).

Output: Returns "Strong" for valid lengths or "Weak" for insufficient lengths.

Design Principle: The tool handles the logic of validation, while the agent handles the communication of the result to the user.

4. Tool–Agent Responsibility Split
Tool: Responsible for the mathematical check of string length.

Agent: Responsible for interpreting the "Strong/Weak" result and providing helpful security advice to the user.
