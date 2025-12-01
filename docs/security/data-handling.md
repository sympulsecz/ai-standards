# Data Handling

Understanding where data flows when using AI systems is critical for security and compliance.

## Data Flow Awareness

When you use AI APIs, data is transmitted to the provider. The prompt may include user input, code, database records, context from your systems, and conversation history.

### Provider Considerations

| Question | Why It Matters |
|----------|----------------|
| Is data logged? | Logs may be accessed or leaked |
| Is data used for training? | Your data improves their models |
| How long is data retained? | Longer retention = longer exposure |
| Where is data processed? | Geographic/regulatory implications |
| Who has access? | Provider employees, subprocessors |

!!! warning "Read Provider Policies"
    Policies vary significantly. Some providers use data for training, some don't. Some retain logs, some don't. Know your provider's data handling before sending sensitive information.

### Enterprise vs. Standard Plans

AI providers often offer enterprise plans with stronger data protections:

**Enterprise plans typically include:**

- No training on your data (vs. standard plans that may use data for model improvement)
- Shorter data retention periods or zero retention options
- Data residency guarantees (data stays in specific regions)
- Business Associate Agreements (BAAs) for HIPAA compliance
- SOC 2 Type II compliance and audit reports
- Priority support and better SLAs
- Advanced security features (SSO, audit logging, access controls)

**Decision factors:**

- Classify your data first—what are you actually sending?
- Compare enterprise vs. standard data handling policies
- Evaluate cost vs. data sensitivity (enterprise plans are more expensive)
- Check if provider's enterprise plan meets your compliance requirements
- Monitor actual usage—are you sending data that requires enterprise protections?

**Practical approach:**

- Start with standard plans for non-sensitive development work
- Upgrade to enterprise when handling internal/confidential data
- Document which teams/projects use which plan tier
- Review regularly as data classification or usage changes

## Data Classification

Categorize data before using with AI:

| Category | Description | Appropriate Use |
|----------|-------------|-----------------|
| **Public** | Already publicly available | Any AI service |
| **Internal** | Business information, not public | AI services with data agreements |
| **Confidential** | Sensitive business data | Self-hosted or strict enterprise agreements |
| **Restricted** | Regulated data (PII, health, financial) | Local models only, or don't use AI |

## Protecting Sensitive Data

### Data Minimization

Only send what's necessary:

```
// Bad: Send entire user record
prompt = "Help with user: " + user.to_json()

// Better: Send only relevant fields
prompt = "Help user " + user.id + " with account type " + user.account_type
```

### Redaction

Remove sensitive information before sending:

```
function redact_pii(text) {
    text = text.replace(/\S+@\S+/g, '[EMAIL]');           // Email addresses
    text = text.replace(/\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g, '[PHONE]');  // Phone numbers
    text = text.replace(/\b\d{3}-\d{2}-\d{4}\b/g, '[SSN]');            // SSN patterns
    return text;
}
```

### Anonymization

Replace identifying information with placeholders:

```
Original:    "John Smith at john@example.com ordered 3 items"
Anonymized:  "[USER_1] at [EMAIL_1] ordered 3 items"
```

### Synthetic Data

Use fake data for development and testing instead of real customer data.

## Self-Hosted Models

For sensitive data, consider local models.

**When appropriate:**

- Regulated industries (healthcare, finance)
- Government/defense
- Highly competitive IP
- Strict data residency requirements

**Trade-offs:**

- Generally lower capability than cloud models
- Infrastructure costs and complexity
- Maintenance burden
- May lack latest features

**Cloud AI appropriate for:**

- General business data
- Public information
- Development/testing
- Non-sensitive applications

## API Key Security

AI API keys are credentials that need protection:

**Storage:**

```
✓ Environment variables
✓ Secrets management systems
✓ Encrypted configuration

✗ Hardcoded in source code
✗ Committed to git
✗ Shared in chat/email
```

**Rotation:**

- After any potential exposure
- On employee offboarding
- On a regular schedule

**Scoping:**

- Use read-only keys when possible
- Set rate limits per key
- Track usage per key

## Compliance Considerations

### GDPR (EU Personal Data)

- Legal basis for processing with AI
- Data subject rights (deletion, access)
- Data transfer mechanisms
- Privacy impact assessments

### HIPAA (Health Data)

- Business Associate Agreements with providers
- Minimum necessary rule
- Audit logging
- Encryption requirements

### SOC 2

- Document AI data flows
- Provider security assessments
- Access controls
- Monitoring and logging

### Industry-Specific

Your industry may have additional requirements (financial services regulations, government data handling, education privacy laws).

## Practical Guidelines

### Before Using AI with Data

1. Classify the data
2. Check provider policies
3. Verify compliance requirements
4. Implement necessary protections
5. Document the data flow

### Data Handling Checklist

- Data is classified appropriately
- Only necessary data is sent
- Sensitive data is redacted/anonymized
- Provider agreement covers the use case
- Compliance requirements are met
- Data flow is documented
- Team is trained on proper handling

### When in Doubt

If unsure whether data should be used with AI:

- Consult security/compliance team
- Default to more restrictive handling
- Document the decision

## Key Takeaways

- Know what data you're sending to AI services and how providers handle it
- Classify data and handle appropriately—don't send restricted data to external services
- Minimize and redact sensitive information before sending
- Consider self-hosted models for sensitive data in regulated industries
- Protect API keys like passwords—use secrets management, rotate regularly
- Understand compliance requirements (GDPR, HIPAA, SOC 2, industry-specific)
- Document data flows and handling decisions
