// API Endpoint - Demo file with security vulnerabilities
// Use this for security review demos

interface DatabaseUser {
	id: string
	email: string
	password: string // ISSUE: Storing plain text password
	role: string
}

// Simulated database
const db = {
	query: async (sql: string): Promise<DatabaseUser[]> => {
		console.log("Executing:", sql)
		return [] // Simulated response
	},
}

// VULNERABLE: Multiple security issues
async function getUser(userId: string): Promise<DatabaseUser | null> {
	// VULNERABILITY 1: SQL Injection
	const query = `SELECT * FROM users WHERE id = '${userId}'`
	const results = await db.query(query)

	// VULNERABILITY 2: Returns sensitive data (password)
	return results[0] || null
}

// VULNERABLE: No input validation
async function searchUsers(searchTerm: string): Promise<DatabaseUser[]> {
	// VULNERABILITY: SQL Injection via search term
	const query = `SELECT * FROM users WHERE email LIKE '%${searchTerm}%'`
	return await db.query(query)
}

// VULNERABLE: Missing authorization check
async function deleteUser(userId: string): Promise<void> {
	// VULNERABILITY: No check if requester can delete this user
	// VULNERABILITY: SQL Injection
	await db.query(`DELETE FROM users WHERE id = '${userId}'`)
}

// Expected AI findings:
// 1. SQL injection (obvious)
// 2. Password exposure (obvious)
// 3. Missing input validation (medium)
// 4. Missing authorization (subtle - AI might miss this)
