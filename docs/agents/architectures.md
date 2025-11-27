# Agent Architectures

Understanding common agent architectures helps you choose the right approach and reason about agent behavior.

## The Basic Agent Loop

At its core, every agent follows a variation of this loop:

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   Observe → Reason → Act → Observe (new state) ─┐   │
│      ▲                                          │   │
│      └──────────────────────────────────────────┘   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

1. **Observe**: Gather information about current state
2. **Reason**: Decide what to do next
3. **Act**: Execute an action (tool call, code execution, etc.)
4. **Repeat**: Until goal is achieved or limits are reached

The differences between architectures lie in how they implement reasoning and action.

## Common Patterns

### ReAct (Reasoning + Acting)

The ReAct pattern interleaves reasoning and acting:

```
Thought: I need to find the user's recent orders
Action: query_database("SELECT * FROM orders WHERE user_id = 123 ORDER BY date DESC LIMIT 5")
Observation: [results returned]
Thought: The user has 3 orders in the last month. I should summarize these.
Action: respond_to_user("You have 3 recent orders: ...")
```

**Key characteristics:**

- Explicit reasoning before each action
- Observations inform next reasoning step
- Traceable decision process

**When to use:**

- Tasks requiring deliberate reasoning
- When you need to understand agent decisions
- Multi-step tasks with dependencies

### Tool Use Pattern

The agent has access to defined tools and decides which to invoke:

```
User: What's the weather like and do I need an umbrella?

Agent reasoning:
- Need weather information → use weather_tool
- Interpret results to answer umbrella question

Tool call: weather_tool(location="user_location")
Response: Based on the forecast showing 80% chance of rain, yes, bring an umbrella.
```

**Key characteristics:**

- Predefined set of available tools
- Agent chooses tools based on task
- Tools provide capabilities the LLM lacks

**When to use:**

- Extending LLM capabilities with external data/actions
- Well-defined operations that should be executed reliably
- When you want controlled access to systems

### Planning Pattern

The agent creates a plan before executing:

```
Goal: Deploy the new feature to production

Plan:
1. Run test suite
2. Check test results
3. If tests pass, create deployment PR
4. Wait for PR approval
5. Merge and deploy

Execution: [follows plan, adapting as needed]
```

**Key characteristics:**

- Upfront planning before action
- May revise plan based on execution results
- Better for complex, multi-step tasks

**When to use:**

- Complex tasks with many steps
- When you want human approval of the plan
- Tasks where order of operations matters

### Reflection Pattern

The agent evaluates its own outputs and improves them:

```
Initial output: [generated code]

Reflection: This code doesn't handle the edge case where the list is empty.

Revised output: [improved code with empty list handling]

Reflection: Now it handles empty lists, but could be more efficient. However, 
efficiency isn't critical here, so this is acceptable.

Final output: [the revised code]
```

**Key characteristics:**

- Self-evaluation of outputs
- Iterative improvement
- Can catch errors before delivery

**When to use:**

- Quality-critical outputs
- Complex generation tasks
- When errors are costly

## Multi-Agent Architectures

### Orchestrator Pattern

One agent coordinates others:

```
┌─────────────────┐
│   Orchestrator  │
│     Agent       │
└────────┬────────┘
         │
    ┌────┴────┬────────────┐
    ▼         ▼            ▼
┌───────┐ ┌───────┐ ┌───────────┐
│ Code  │ │ Test  │ │ Document  │
│ Agent │ │ Agent │ │ Agent     │
└───────┘ └───────┘ └───────────┘
```

**When to use:**

- Complex workflows with distinct phases
- When different capabilities are needed for different steps
- Separation of concerns is valuable

### Debate/Adversarial Pattern

Multiple agents with different perspectives:

```
┌──────────────────────────────────────────┐
│                                          │
│  Proposer ◄──────────► Critic           │
│     │                     │              │
│     └────────┬────────────┘              │
│              ▼                           │
│         Final Output                     │
│                                          │
└──────────────────────────────────────────┘
```

**When to use:**

- When you want to surface potential issues
- Quality-critical decisions
- Reducing blind spots in analysis

## Architecture Selection

| Consideration | Suggested Pattern |
|---------------|-------------------|
| Simple tool augmentation | Tool use |
| Complex reasoning needed | ReAct |
| Multi-step workflows | Planning |
| Quality-critical outputs | Reflection |
| Distinct capability phases | Multi-agent orchestration |
| Need diverse perspectives | Debate/adversarial |

## Practical Considerations

### State Management

Agents need to track:

- Conversation/interaction history
- Task progress
- Intermediate results
- Context that persists across steps

Consider how state is stored and what happens if the agent is interrupted.

### Error Handling

Agents will encounter errors. Plan for:

- Tool call failures
- Unexpected responses
- Timeouts
- Rate limits
- Invalid states

### Cost and Latency

Agent loops involve multiple LLM calls. Consider:

- Each iteration has cost and latency
- Complex reasoning = more tokens = higher cost
- Parallel actions where possible
- Caching opportunities

### Observability

Agent behavior should be observable:

- Log reasoning steps
- Track tool calls and results
- Record decision points
- Enable debugging of failures

## Key Takeaways

- All agents follow an observe-reason-act loop
- Different patterns suit different task types
- Multi-agent architectures help with complex workflows
- Consider state, errors, cost, and observability in your design
- Start simple; add complexity only when needed
