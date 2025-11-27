# Data Handling

Understanding where data flows when using AI systems is critical for security and compliance.

## Data Flow Awareness

### What Gets Sent to AI Services?

When you use AI APIs, data is transmitted:

```
Your System                              AI Provider
     │                                        │
     │──── Prompt (includes context) ────────►│
     │                                        │
     │◄─── Response ──────────────────────────│
     │                                        │
```

The prompt may include:

- User input
- Code or documents for analysis
- Database records
- Context from your systems
- Conversation history

### Data at the Provider

Once data reaches an AI provider, consider:

| Question | Why It Matters |
|----------|----------------|
| Is data logged? | Logs may be accessed or leaked |
| Is data used for training? | Your data improves their models |
| How long is data retained? | Longer retention = longer exposure |
| Where is data processed? | Geographic/regulatory implications |
| Who has access? | Provider employees, subprocessors |

!!! warning "Read the Terms"
    Provider policies vary significantly. Some use data for training, some don't. Some retain logs, some don't. Know your provider's policies.

## Data Classification

Categorize data before using with AI:

### Categories

**Public**

- Already publicly available
- No restrictions on sharing
- Safe to use with any AI service

**Internal**

- Not public but not sensitive
- Business information
- May use with appropriate provider agreements

**Confidential**

- Sensitive business data
- Requires protection
- Use only with strict data agreements or local models

**Restricted**

- Highly sensitive
- Regulated data (PII, health, financial)
- Generally should not use with external AI services

### Handling by Category

```
Public       → Any AI service
Internal     → AI services with data agreements
Confidential → Self-hosted or strict enterprise agreements
Restricted   → Local models only, or don't use AI
```

## Protecting Sensitive Data

### Data Minimization

Only send what's necessary:

```python
# Bad: Send entire user record
prompt = f"Help with user: {user.to_json()}"

# Better: Send only relevant fields
prompt = f"Help user {user.id} with account type {user.account_type}"
```

### Redaction

Remove sensitive information before sending:

```python
def redact_pii(text):
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    # Remove phone numbers
    text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', text)
    # Remove SSN patterns
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', text)
    return text
```

### Anonymization

Replace identifying information with placeholders:

```python
# Original
"John Smith at john@example.com ordered 3 items"

# Anonymized
"[USER_1] at [EMAIL_1] ordered 3 items"
```

### Synthetic Data

Use fake data for development and testing:

```python
# Instead of real customer data, use generated data
test_users = [
    generate_fake_user() for _ in range(100)
]
```

## Self-Hosted Models

For sensitive data, consider local models:

### Advantages

- Data never leaves your infrastructure
- Full control over logging and retention
- No third-party data agreements needed
- May be required for compliance

### Trade-offs

- Generally lower capability than cloud models
- Infrastructure costs and complexity
- Maintenance burden
- May lack latest features

### When to Use

```
Self-hosted appropriate:
- Regulated industries (healthcare, finance)
- Government/defense
- Highly competitive IP
- Strict data residency requirements

Cloud AI appropriate:
- General business data
- Public information
- Development/testing
- Non-sensitive applications
```

## API Key Security

AI API keys are credentials that need protection:

### Storage

```
✓ Environment variables
✓ Secrets management systems
✓ Encrypted configuration

✗ Hardcoded in source code
✗ Committed to git
✗ Shared in chat/email
```

### Rotation

Rotate API keys regularly:

- After any potential exposure
- On employee offboarding
- On a regular schedule

### Scoping

Use least-privilege keys when available:

- Read-only vs. full access
- Rate limits per key
- Usage tracking per key

## Compliance Considerations

### GDPR

If processing EU personal data:

- Legal basis for processing with AI
- Data subject rights (deletion, access)
- Data transfer mechanisms
- Privacy impact assessments

### HIPAA

If processing health data:

- Business Associate Agreements with providers
- Minimum necessary rule
- Audit logging
- Encryption requirements

### SOC 2

If you need SOC 2 compliance:

- Document AI data flows
- Provider security assessments
- Access controls
- Monitoring and logging

### Industry-Specific

Your industry may have additional requirements:

- Financial services regulations
- Government data handling
- Education privacy laws

## Practical Guidelines

### Before Using AI with Data

1. Classify the data
2. Check provider policies
3. Verify compliance requirements
4. Implement necessary protections
5. Document the data flow

### Data Handling Checklist

- [ ] Data is classified
- [ ] Only necessary data is sent
- [ ] Sensitive data is redacted/anonymized
- [ ] Provider agreement covers the use
- [ ] Compliance requirements are met
- [ ] Data flow is documented
- [ ] Team is trained on handling

### When in Doubt

If you're unsure whether data should be used with AI:

- Consult security/compliance team
- Default to more restrictive handling
- Document the decision

## Key Takeaways

- Know what data you're sending to AI services
- Classify data and handle appropriately
- Minimize and redact sensitive information
- Consider self-hosted models for sensitive data
- Protect API keys like passwords
- Understand compliance requirements
- Document data flows and decisions
