# Safety and Guardrails

Agents that can take actions can also cause harm. This section covers patterns for building safe, controllable agents.

## The Safety Mindset

When building agents, assume they will:

- Misinterpret instructions
- Take unintended actions
- Encounter situations you didn't anticipate
- Be given malicious inputs
- Fail in unexpected ways

Design with these assumptions in mind.

## Layers of Defense

Safe agent design uses multiple layers:

```
┌─────────────────────────────────────────────────────────┐
│                    Human Oversight                       │
├─────────────────────────────────────────────────────────┤
│                    Action Limits                         │
├─────────────────────────────────────────────────────────┤
│                    Tool Permissions                      │
├─────────────────────────────────────────────────────────┤
│                    Input Validation                      │
├─────────────────────────────────────────────────────────┤
│                    Agent Core Logic                      │
└─────────────────────────────────────────────────────────┘
```

Each layer catches different types of problems.

## Human Oversight

The most important guardrail is keeping humans in the loop.

### Approval Workflows

Require human approval for high-impact actions:

```
Low risk (auto-approve):
- Read-only queries
- Sending informational messages
- Generating drafts

Medium risk (notify):
- Creating records
- Sending external communications
- Modifying non-critical data

High risk (require approval):
- Deleting data
- Financial transactions
- Modifying permissions
- Actions affecting many users
```

### Checkpoints

Build natural stopping points:

```
Agent: "I've identified 47 files that need updating. 
Here's my plan: [summary]

Should I proceed, or would you like to review the 
full list first?"
```

### Override Capability

Ensure humans can always:

- Stop agent execution
- Reverse actions taken
- Take manual control
- Access what the agent was doing

## Action Limits

Constrain what agents can do:

### Rate Limits

Prevent runaway execution:

- Maximum actions per minute
- Maximum tool calls per task
- Maximum tokens consumed

### Scope Limits

Restrict agent reach:

- Files/directories it can access
- Systems it can interact with
- Data it can modify

### Impact Limits

Bound potential damage:

- Maximum records affected per action
- Maximum monetary value per transaction
- Maximum users impacted

### Time Limits

Prevent endless execution:

- Maximum runtime per task
- Timeout on individual operations
- Automatic termination after inactivity

## Tool Permissions

Not all tools should be available to all agents in all contexts.

### Permission Levels

```
Read-only tools:
- search_documents
- get_user_info
- list_files

Write tools (elevated):
- update_record
- send_email
- create_file

Destructive tools (restricted):
- delete_record
- modify_permissions
- execute_command
```

### Context-Dependent Access

Adjust available tools based on:

- User permissions
- Task type
- Environment (production vs. staging)
- Time of day or day of week

### Tool Wrappers

Wrap dangerous tools with safety logic:

```python
def safe_delete_record(record_id):
    # Check permissions
    if not current_user_can_delete(record_id):
        raise PermissionError("Not authorized")
    
    # Check impact
    if is_critical_record(record_id):
        raise SafetyError("Cannot delete critical records")
    
    # Log before action
    log_action("delete_attempt", record_id)
    
    # Soft delete instead of hard delete
    return soft_delete(record_id)
```

## Input Validation

Validate everything the agent works with.

### User Input

Don't trust user input:

- Validate format and content
- Check for injection attempts
- Sanitize before processing

### Tool Outputs

External systems may return unexpected data:

- Validate response format
- Check for reasonable values
- Handle missing or malformed data

### Agent Decisions

Validate the agent's own decisions:

- Is this tool call well-formed?
- Are parameters within acceptable ranges?
- Does this action make sense given the context?

## Preventing Common Failures

### Infinite Loops

Detect and prevent:

```
Loop detection:
- Track recent actions
- Flag if same action repeated N times
- Require different approach or escalate
```

### Privilege Escalation

Prevent agents from gaining capabilities:

- Fixed tool set (can't add tools)
- Fixed permissions (can't modify own access)
- No access to modify own prompts

### Resource Exhaustion

Prevent cost/resource runaway:

- Token budgets
- API call limits
- Compute time limits

### Data Exfiltration

Prevent unauthorized data access:

- Audit data access
- Limit what can be included in outputs
- Monitor for unusual data patterns

## Monitoring and Alerting

Active monitoring catches issues:

### What to Monitor

| Metric | Why |
|--------|-----|
| Action rate | Detect runaway agents |
| Error rate | Identify failing agents |
| Token consumption | Cost control |
| Unusual patterns | Potential misuse |
| Sensitive data access | Security concerns |

### Alerting Thresholds

Set alerts for:

- Action rate exceeds threshold
- Error rate spikes
- Cost exceeds budget
- Sensitive action attempted
- Agent running longer than expected

## Incident Response

Plan for when things go wrong:

### Immediate Response

1. Stop the agent
2. Assess damage
3. Notify relevant parties
4. Preserve logs and state

### Investigation

1. What happened?
2. Why did guardrails fail?
3. What was the impact?
4. How do we prevent recurrence?

### Remediation

1. Reverse harmful actions if possible
2. Update guardrails
3. Test fixes
4. Document lessons learned

## Testing Safety

### Adversarial Testing

Test with malicious inputs:

- Prompt injection attempts
- Requests for forbidden actions
- Edge cases and unusual inputs

### Failure Mode Testing

Test guardrail effectiveness:

- Do limits actually limit?
- Can approval be bypassed?
- Do alerts fire correctly?

### Chaos Testing

Test resilience:

- What if tools fail?
- What if limits are hit?
- What if external systems are down?

## Key Takeaways

- Assume agents will misbehave; design for it
- Use multiple layers of defense
- Keep humans in the loop for high-impact decisions
- Limit what agents can do, not just what they should do
- Monitor actively and alert on anomalies
- Plan for incidents before they happen
- Test your safety measures
