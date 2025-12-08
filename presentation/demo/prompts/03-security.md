# Security Review Prompts

## Part 1: General Security Review

Use with `code/vulnerable-api.ts`:

```
Review this API endpoint for security vulnerabilities:

[paste the code]
```

**Expected findings:**
- SQL injection vulnerability (string concatenation in query)
- Missing input validation
- Sensitive data exposure (returning password field)
- No rate limiting consideration

**Intentionally subtle issue AI might miss:**
- The endpoint allows querying any user by ID without authorization check

---

## Part 2: Targeted Security Review

### SQL Injection Focus

```
Check this database query for SQL injection vulnerabilities:

const query = `SELECT * FROM users WHERE id = ${userId}`;
```

### Input Validation Focus

```
What input validation is missing from this API endpoint?

[paste code]

Consider: types, ranges, formats, and malicious input
```

### Data Exposure Focus

```
What sensitive data might this endpoint accidentally expose?

[paste code]
```

---

## Part 3: Discussing Findings

After AI identifies issues, use these follow-up prompts:

### Understanding the Risk

```
Explain how an attacker could exploit the SQL injection vulnerability you found.
Keep it simple - assume I'm not a security expert.
```

### Getting the Fix

```
Show me how to fix the SQL injection using parameterized queries.
```

### Verification

```
Is this fixed version secure?

[paste proposed fix]
```

---

## Part 4: Security Limitations Discussion

Use this to demonstrate AI limitations:

```
Is this API endpoint secure?

async function getUserOrders(userId: string, requestingUserId: string) {
  const orders = await db.query(
    'SELECT * FROM orders WHERE user_id = $1',
    [userId]
  );
  return orders;
}
```

**What to point out:**
- AI will likely say "yes, parameterized query is safe"
- But: there's no check that `requestingUserId` can access `userId`'s orders
- This is a business logic / authorization issue AI can't catch without context

---

## Security Review Recap

**AI is good at:**
- Pattern matching (SQL injection, XSS patterns)
- Known vulnerability signatures
- Missing standard validations

**AI is NOT good at:**
- Authorization logic
- Business rule violations
- Context-dependent security decisions
- Novel attack vectors

**Key message:** AI is a helpful first pass, not a replacement for security expertise.

