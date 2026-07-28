...

# Hacker Holidays 2026 — Day 1
<br><br><br>

**Room:** The Concierge Knows Too Much ( https://tryhackme.com/room/hh-theconciergeknows-2d7eb4d9 )  
**Platform:** TryHackMe  
**Difficulty:** Very Easy  
**Category:** AI / Prompt Injection  
**Written:** 28 July 2026  

<br>

## Description

This writeup documents my methodology for solving an AI-agent challenge by analyzing the chatbot's trust model, forming hypotheses from its responses, and iteratively refining prompts instead of relying on random prompt injection attempts.

<br>

## Behavioral Recon

Before attempting any structured prompt injection, I started with a simple interaction to establish the chatbot's default behavior. My initial assumption was that one of two outcomes would occur:

- The chatbot might accidentally disclose the requested information.
- If it refused, the refusal itself could reveal useful details about its internal access controls.

<br><br>
![Initial Interaction](images/wrhhd1-1.png)
<br><br>

## Trust Discovery

The room description and the chatbot's initial response indicated that the assistant relied on a trust model rather than simply rejecting sensitive requests. To understand how this trust was established, I directly asked the chatbot who it trusted.

<br><br>
![Trust Discovery](images/wrhhd1-2.png)
<br><br>

**Analysis:**  The chatbot revealed the existence of several VIP guests and even disclosed their names. This confirmed that privileged users existed and suggested that the chatbot differentiated users based on identity.  

Based on this observation, I formed the hypothesis that assuming the identity of a VIP guest might alter the chatbot's behavior. I then claimed to be a VIP guest to test this assumption.

<br>

## Identity Claim

Once the chatbot asked me to identify which VIP guest I was, I selected one of the previously disclosed VIP names.

The chatbot immediately accepted the claimed identity and personalized its response without requesting any form of verification. This indicated that the trust model relied solely on a user-supplied identifier rather than validating the user's identity.

Although the impersonation was successful, directly requesting the flag still resulted in a refusal. This suggested that VIP status alone was insufficient to bypass the chatbot's restrictions, requiring a different approach.

<br><br>
![identity](images/wrhhd1-3.png)
<br><br>

<br>

## Escalation via Reframing

Instead of repeating the same request, I refined the prompt to align with the established trust context. I explicitly referenced my verified VIP identity and requested the Flag within that context.

The chatbot disclosed the requested information, including the escalation Flag code and its internal instructions, completing the challenge.

<br><br>
![reframed-prompt](images/wrhhd1-4.png)
<br><br>

<br><br>
![flag](images/wrhhd1-5.png)
<br><br>



<br>

## Lessons Learned

- Initial refusals can reveal valuable information about an AI agent's authorization logic.
- Reconnaissance should always come before exploitation.
- Small behavioral clues are often more valuable than aggressive prompt injection attempts.
- Forming and testing hypotheses is more effective than repeatedly sending random prompts.
- Prompt framing can significantly influence an AI agent's response, even after authentication.


**Final Thoughts:-** This room provides a practical introduction to AI security concepts, particularly trust modeling and prompt refinement.


<br><br><br>

---


All Hail....

— **Nanashi Bx2** -- Security Researcher 