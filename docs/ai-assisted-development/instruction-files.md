# Instruction Files

You've learned workflows for code review, debugging, and refactoring. Now encode these patterns and preferences into instruction files so AI tools automatically follow your project's conventions.

!!! info "Building on Workflows"
    The workflows covered in [Tool Use: Workflows](tool-use-workflows.md) work better when AI understands your project conventions. Instruction files provide that context automatically, reducing the need to specify conventions in every prompt.

## Why Instruction Files Matter

Without project-specific guidance, AI tools default to generic patterns that may not match your codebase. Instruction files configure AI tools to follow your project's conventions, similar to how configuration files (`.eslintrc`, `prettier.config.js`, `build.gradle`) guide linters, formatters, and build tools.

The key difference: linters and formatters enforce rules mechanically, while AI tools interpret instructions and apply them contextually.

## Common File Names

Different tools use different conventions:

- **`CLAUDE.md`** - Used by Claude Code and read by Claude when processing the project
- **`.cursorrules`** - Used by Cursor
- **`.github/copilot-instructions.md`** - Used by GitHub Copilot
- **`AGENTS.md`** or `.ai/` directory - Emerging conventions for agent-based tools

Some projects maintain a single instruction file that works across tools. The important part is content, not filename.

## What to Include

### Coding Style and Conventions

Specify language features, formatting preferences, and naming patterns.

**Example:**

```markdown
## Language and Style

- Use TypeScript strict mode throughout
- Prefer functional components with hooks over class components
- Use async/await over raw promises
- Error handling: return Result<T, Error> types, don't throw exceptions

## Naming Conventions

- Components: PascalCase (UserProfile.tsx)
- Hooks: camelCase starting with 'use' (useUserData.ts)
- Utilities: camelCase (formatCurrency.ts)
- Constants: UPPER_SNAKE_CASE
```

!!! tip "Be Specific About Existing Code"
    ❌ "Use our authentication utilities"

    ✅ "Use `requireAuth` middleware from src/middleware/auth.ts for protected routes"

### Project Structure Patterns

Explain where different types of files live and how they're organized:

```markdown
## File Organization

- Components go in `src/components/`
- Each component gets its own directory with: Component.tsx, Component.test.tsx, Component.module.css
- Business logic lives in `src/services/`
- API clients extend BaseClient from `src/api/base.ts`
- Tests use `__tests__` directories alongside source files
```

### Existing Abstractions and Utilities

Point AI to existing code that should be reused rather than recreated:

```markdown
## Existing Utilities

- HTTP requests: Use `fetchWithRetry` from `src/utils/http.ts`, not raw fetch
- Date formatting: Use `formatDate` from `src/utils/dates.ts`
- Form validation: Use Zod schemas in `src/schemas/`
- Database queries: Use Prisma client instance from `src/db/client.ts`
```

### Framework and Library Patterns

Specify how to use frameworks and libraries in your project.

**Example:**

```markdown
## React Patterns

- State management: Use Zustand stores in `src/stores/`
- Data fetching: Use React Query hooks
- Routing: Use Next.js App Router (app directory)
- Forms: Use React Hook Form with Zod validation

## API Patterns

- All endpoints return `{ data: T } | { error: string }`
- Use middleware from `src/middleware/` for auth, logging, etc.
- Input validation happens in endpoint handlers using Zod
```

!!! tip "Show Examples for Complex Patterns"
    ```typescript
    // API endpoints follow this structure:
    export async function GET(req: NextRequest) {
      try {
        const data = await service.fetchData();
        return NextResponse.json({ data });
      } catch (error) {
        return NextResponse.json({ error: error.message }, { status: 500 });
      }
    }
    ```

### Testing Conventions

Describe test structure and expectations:

```markdown
## Testing

- Use Vitest for unit tests
- Test files: `ComponentName.test.tsx`
- Mock external services using factories from `src/test/factories/`
- Integration tests go in `src/test/integration/`
- Aim for clear test descriptions: describe behavior, not implementation
```

### Context Management

Specify what files to include or exclude from AI context:

```markdown
## Files to Exclude

- Generated code in `src/generated/`
- Third-party SDKs in `src/vendor/`
- Large data files in `data/`
- Build artifacts in `dist/`, `build/`

## Priority Files

When understanding this codebase, start with:
- Architecture overview: `docs/architecture.md`
- Core types: `src/types/core.ts`
- Main workflows: `src/services/workflow.ts`
```

## Team Adoption

Commit instruction files to your repository so all developers and AI tools use consistent conventions. Review and update them during team meetings, reference them in code review when AI-generated code doesn't match conventions, and keep them synchronized with actual codebase evolution.

When AI consistently misunderstands a pattern, note what went wrong, add clarifying guidance to the instruction file, test that the new instruction improves results, and share the update with the team.

## Practical Example

### TypeScript/Node.js API

```markdown
# AI Coding Instructions

## Project Overview

Node.js API using TypeScript, Express, Prisma ORM, and PostgreSQL.

## Code Style

- TypeScript strict mode enabled
- Use async/await, not callbacks or raw promises
- Prefer named exports over default exports
- Use `const` for all declarations unless reassignment needed

## Project Structure

- Routes in `src/routes/` - one file per resource
- Business logic in `src/services/`
- Data access in `src/repositories/`
- DTOs and types in `src/types/`
- Middleware in `src/middleware/`

## Naming Conventions

- Files: kebab-case (`user-service.ts`, `order-routes.ts`)
- Classes: PascalCase (`UserService`, `OrderRepository`)
- Functions/variables: camelCase (`createUser`, `findById`)
- Constants: UPPER_SNAKE_CASE (`MAX_RETRIES`, `API_VERSION`)

## Error Handling

- Use custom error classes from `src/errors/`
- All routes wrapped with `asyncHandler` middleware
- Return errors as `{ error: string, code: string }`
- Log errors with context using Winston logger

## API Patterns

- All responses follow `ApiResponse<T>` type from `src/types/api.ts`
- Use Zod for request validation
- Middleware chain: auth → validation → rate limiting → handler
- Endpoints return 200 for success, appropriate 4xx/5xx for errors

## Database

- Prisma for all database access
- Migrations in `prisma/migrations/`
- Use transactions for multi-step operations
- Repository pattern: see `src/repositories/user.repository.ts`

## Testing

- Vitest for unit tests
- Supertest for integration tests
- Test files: `*.test.ts` alongside source
- Mock external services using `src/test/mocks/`

## Code to Reference

- Base repository: `src/repositories/base.repository.ts`
- Auth middleware: `src/middleware/auth.ts`
- Error handling: `src/middleware/error-handler.ts`

## Files to Ignore

- `dist/` - compiled output
- `node_modules/`
- `prisma/generated/` - Prisma client
- `.env` files - never include in context
```

## Key Takeaways

**Avoid vague guidance:**

```markdown
❌ "Write good code"
❌ "Follow best practices"
❌ "Be consistent"
```

**Don't document everything:**

```markdown
❌ [50 pages of comprehensive style guide]
✅ [Focus on project-specific patterns that differ from defaults]
```

**Don't contradict tooling:**

```markdown
❌ Instruction file says: "Use 2 spaces"
❌ .editorconfig says: "Use 4 spaces"
✅ Let EditorConfig handle formatting, instruction file covers patterns
```

Instruction files work best when they specify project-specific patterns, reference existing code to reuse, and remain synchronized with actual codebase evolution. Well-maintained instruction files reduce friction between AI-generated code and project standards, making AI assistance more valuable with less review overhead.
