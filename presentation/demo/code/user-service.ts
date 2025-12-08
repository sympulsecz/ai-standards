// User Service - Demo file for prompting exercises
// This is a clean starting point for iterative prompting demos

interface User {
	id: string
	email: string
	name: string
	isVerified: boolean
	createdAt: Date
}

// Sample data for testing
const users: User[] = [
	{
		id: "1",
		email: "alice@example.com",
		name: "Alice",
		isVerified: true,
		createdAt: new Date("2024-01-15"),
	},
	{
		id: "2",
		email: "bob@example.com",
		name: "Bob",
		isVerified: false,
		createdAt: new Date("2024-02-20"),
	},
	{
		id: "3",
		email: "carol@example.com",
		name: "Carol",
		isVerified: true,
		createdAt: new Date("2024-03-10"),
	},
]

/**
 * Returns all users who have verified their email address.
 * Results are sorted alphabetically by email.
 */
function getVerifiedUsers(userList: User[]): User[] {
	return userList
		.filter((user) => user.isVerified)
		.sort((a, b) => a.email.localeCompare(b.email))
}

// Use this file to demonstrate:
// 1. Adding new functions with specific prompts
// 2. Iterative refinement (add feature -> refine -> add validation)
// 3. Documentation generation
