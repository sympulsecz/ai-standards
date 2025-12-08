// Shopping Cart - Demo file with intentional bugs
// Use this for code review and debugging demos

interface CartItem {
	id: string
	name: string
	price: number
	quantity: number
}

class ShoppingCart {
	private items: CartItem[] = []

	addItem(item: CartItem): void {
		const existing = this.items.find((i) => i.id === item.id)
		if (existing) {
			existing.quantity += item.quantity
		} else {
			this.items.push(item)
		}
	}

	// BUG: Off-by-one error - uses index instead of finding by id
	removeItem(itemId: string): void {
		const index = this.items.findIndex((i) => i.id === itemId)
		this.items.splice(index, 1) // What if index is -1?
	}

	// BUG: Crashes on empty cart
	getTotal(): number {
		return this.items.reduce((sum, item) => {
			return sum + item.price * item.quantity
		}, 0)
	}

	// BUG: No validation on quantity
	updateQuantity(itemId: string, quantity: number): void {
		const item = this.items.find((i) => i.id === itemId)
		if (item) {
			item.quantity = quantity // What if quantity is negative?
		}
	}

	getItems(): CartItem[] {
		return this.items
	}
}

// Test scenario that triggers bugs:
// 1. Add an item
// 2. Remove an item that doesn't exist (index = -1, splice removes last item)
// 3. Update quantity to -5 (creates negative total)
