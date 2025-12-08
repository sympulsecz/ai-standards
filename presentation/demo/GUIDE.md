# Demo Guide

A 50-minute live demonstration following the presentation. This guide provides everything you need to run an effective demo.

## Before You Start

### Pre-Demo Checklist

- [ ] AI tool is open and logged in (Cursor, ChatGPT, Claude, or Copilot)
- [ ] Demo code files are open in your editor
- [ ] Font size is large enough for the room (16-18pt minimum)
- [ ] Dark theme enabled (easier to read on projectors)
- [ ] Close notifications and other distracting windows
- [ ] Have this guide open on a second screen or printed

### If Something Goes Wrong

- **AI gives wrong answer**: "This is actually a great example of why we verify AI output. Let me try rephrasing..."
- **AI is slow**: "While we wait, let me explain what we're asking for..."
- **AI hallucinates**: "Notice how confident that sounds? This is exactly why we don't blindly trust AI."
- **Technical issues**: Switch to backup tool or use pre-recorded screenshots

---

## Timeline Overview

| Time | Section | Key Message |
|------|---------|-------------|
| 0-15 min | Effective Prompting | Specificity and iteration matter |
| 15-30 min | Code Review & Debug | AI as a first-pass reviewer |
| 30-40 min | Workflow Integration | Quick wins for daily work |
| 40-50 min | Security Review | AI catches patterns, humans make decisions |

---

## Section 1: Effective Prompting (15 min)

### Goal

Show the difference between vague and specific prompts, then demonstrate iterative refinement.

### What to Focus On

- The dramatic quality difference between vague and specific prompts
- How 2-3 iterations typically get you to a good result
- Talking through your thought process as you refine

### What to Avoid

- Spending too long on a perfect first prompt (iteration is the point)
- Complex domain-specific examples the audience won't understand
- Getting derailed by AI's creative suggestions

### Demo Steps

1. **Show a vague prompt** (use `prompts/01-prompting.md`)
   - Ask: "Write a function to get users"
   - Point out: The AI will produce something, but probably not what you need

2. **Show the specific version**
   - Ask: "Write a TypeScript function that takes an array of User objects and returns only those with verified email addresses"
   - Point out: Same task, dramatically better result

3. **Demonstrate iteration** (use `code/user-service.ts`)
   - Start with a reasonable request
   - When AI responds, ask for a specific improvement
   - Show how each iteration builds on the previous

### Talking Points

> "Notice how I didn't get it perfect on the first try - that's normal. The goal isn't a perfect prompt, it's a productive conversation."

> "I'm being specific about the outcome, not the method. AI is better at figuring out HOW when you're clear about WHAT."

---

## Section 2: Code Review & Debugging (15 min)

### Goal

Show AI as a first-pass code reviewer and debugging assistant.

### What to Focus On

- The structured way to present code for review
- How AI catches things humans might miss (and vice versa)
- Using AI to interpret cryptic error messages

### What to Avoid

- Pretending AI catches everything (it doesn't)
- Complex bugs that require deep context
- Spending too long on a single issue

### Demo Steps

1. **Code Review** (use `code/buggy-cart.ts`)
   - Paste the code and ask: "Review this shopping cart code for potential issues"
   - Let AI find the off-by-one error or empty cart issue
   - Point out: AI is good at pattern matching, not business logic

2. **Debugging with context**
   - Show the structured debugging prompt from `prompts/02-code-review.md`
   - Demonstrate how providing error message + trigger + code gets better results

3. **The verification step**
   - After AI suggests a fix, walk through WHY it's correct
   - Emphasize: "I'm verifying this makes sense, not just accepting it"

### Talking Points

> "AI just saved me 10 minutes of staring at this code. But I still need to verify the fix is correct."

> "Notice I'm not dumping the entire codebase - just the relevant 30 lines. Context quality matters more than quantity."

---

## Section 3: Workflow Integration (10 min)

### Goal

Quick demonstration of practical daily workflow improvements.

### What to Focus On

- Speed and convenience of these tasks
- How AI handles tedious but important documentation
- The "augment, don't replace" principle in action

### What to Avoid

- Deep diving into any single workflow
- Complex CI/CD setup discussions
- Tool-specific features that don't generalize

### Demo Steps

1. **PR Description Generation**
   - Show a small code diff (or use the changes you made in previous demos)
   - Ask AI to generate a PR description
   - Point out: "I'll review and edit this, but it's a great starting point"

2. **Commit Message**
   - Ask AI to suggest a commit message for a change
   - Show how you'd refine it to match team conventions

3. **Quick Documentation**
   - Take a function from the demo and ask for JSDoc comments
   - Point out: "Documentation is where AI really shines - tedious for humans, easy for AI"

### Talking Points

> "These aren't revolutionary features - they're time savers. Five minutes here, ten minutes there, it adds up."

> "I always review what AI generates for external-facing content. My name is on this PR, not the AI's."

---

## Section 4: Security Review (10 min)

### Goal

Show AI as a security-aware reviewer, while emphasizing human judgment.

### What to Focus On

- Common vulnerability patterns AI can catch
- The importance of not relying solely on AI for security
- Practical guidance for day-to-day security awareness

### What to Avoid

- Implying AI is a replacement for security expertise
- Complex attack scenarios
- Tool-specific security features

### Demo Steps

1. **Review vulnerable code** (use `code/vulnerable-api.ts`)
   - Paste the code and ask: "Review this API endpoint for security issues"
   - AI should catch: SQL injection, missing input validation, potential data exposure

2. **Walk through findings**
   - For each issue AI identifies, explain WHY it's a problem
   - Point out anything AI missed (there's intentionally one subtle issue)

3. **Discuss the limits**
   - "AI caught the obvious SQL injection, but would it catch a complex business logic flaw?"
   - Emphasize: "This is a first pass, not a replacement for security review"

### Talking Points

> "AI is great at pattern matching - 'this looks like SQL injection' is exactly the kind of thing it's good at."

> "But notice what AI can't do: it can't tell me if this endpoint SHOULD exist, or if the data it returns is appropriate for this user."

---

## Handling Questions

### Common Questions and Responses

**"Which AI tool is best?"**
> "They all have strengths. The patterns we're discussing work across tools. Pick one your team is comfortable with and learn it well."

**"Isn't this cheating / making us lazy?"**
> "Is using a calculator cheating at math? These are tools. The thinking and verification is still your job."

**"What about code ownership / liability?"**
> "You're responsible for code you commit, regardless of how you wrote it. AI is like Stack Overflow - helpful, but you own the result."

**"How do you handle sensitive code?"**
> "Know your organization's policy. Many tools offer enterprise versions with data privacy guarantees. When in doubt, redact sensitive parts."

**"Will AI replace developers?"**
> "AI changes HOW we work, not WHETHER we work. It handles tedious tasks so we can focus on the interesting problems."

---

## Backup Plans

### If AI Tool is Down

- Use screenshots from a previous successful run
- Walk through the prompts explaining what you WOULD see
- "Let me show you what this typically produces..."

### If Demo Code Doesn't Work

- Have the expected outputs saved in a separate file
- Show the input, then show the output
- Focus on the process, not the live result

### If Running Out of Time

- Priority order: Prompting > Code Review > Security > Workflow
- Each section can be shortened by skipping iteration examples
- The key messages matter more than completing every step

---

## After the Demo

- Ask for questions
- Point people to the documentation site for more details
- Offer to help individuals get set up with tools
- Collect feedback on what was most/least useful
