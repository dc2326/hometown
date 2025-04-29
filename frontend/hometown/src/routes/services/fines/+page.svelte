<script>
    let activeTickets = [
        {
            id: 'TKT-2024-001',
            type: 'Parking Violation',
            date: '2024-04-15',
            location: '123 Main St',
            amount: 45.00,
            dueDate: '2024-05-15',
            status: 'Unpaid'
        },
        {
            id: 'TKT-2024-002',
            type: 'Traffic Violation',
            date: '2024-04-20',
            location: '456 Oak Ave',
            amount: 150.00,
            dueDate: '2024-05-20',
            status: 'Unpaid'
        }
    ];

    let paymentHistory = [
        {
            id: 'TKT-2023-045',
            type: 'Parking Violation',
            date: '2023-12-01',
            amount: 35.00,
            status: 'Paid'
        }
    ];

    function payTicket(ticketId) {
        // Handle payment logic here
        console.log('Paying ticket:', ticketId);
    }

    function viewDetails(ticketId) {
        // Handle view details logic here
        console.log('Viewing details for ticket:', ticketId);
    }
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --accent-gold: #d4af37;
        --background: #f5f5f0;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
    }

    .fines-container {
        max-width: 800px;
        margin: 2rem auto;
        padding: 0 1rem;
        background: var(--background);
        min-height: 100vh;
    }

    .section {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(45, 90, 39, 0.1);
        position: relative;
        overflow: hidden;
    }

    .section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: var(--primary-green);
    }

    .section-title {
        color: var(--primary-green);
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .ticket-card {
        border: 1px solid rgba(45, 90, 39, 0.1);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1rem;
        background: var(--card-bg);
        box-shadow: var(--card-shadow);
    }

    .ticket-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .ticket-id {
        color: var(--primary-green);
        font-weight: 600;
    }

    .ticket-status {
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }

    .status-unpaid {
        background: #fff0f0;
        color: #e74c3c;
    }

    .status-paid {
        background: #f0fff0;
        color: var(--primary-green);
    }

    .ticket-details {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin-bottom: 1rem;
    }

    .detail-item {
        margin-bottom: 0.5rem;
    }

    .detail-label {
        color: var(--text-muted);
        font-size: 0.9rem;
    }

    .detail-value {
        font-weight: 600;
        color: var(--primary-green);
    }

    .button-group {
        display: flex;
        gap: 1rem;
    }

    .btn {
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        border: none;
        transition: all 0.3s;
    }

    .btn-primary {
        background: var(--primary-green);
        color: white;
    }

    .btn-secondary {
        background: var(--accent-gold);
        color: white;
    }

    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(43, 43, 43, 0.2);
    }
</style>

<div class="fines-container">
    <div class="section">
        <h2 class="section-title">Active Tickets</h2>
        {#each activeTickets as ticket}
            <div class="ticket-card">
                <div class="ticket-header">
                    <span class="ticket-id">{ticket.id}</span>
                    <span class="ticket-status status-{ticket.status.toLowerCase()}">{ticket.status}</span>
                </div>
                <div class="ticket-details">
                    <div class="detail-item">
                        <div class="detail-label">Type</div>
                        <div class="detail-value">{ticket.type}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Date</div>
                        <div class="detail-value">{ticket.date}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Location</div>
                        <div class="detail-value">{ticket.location}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Amount</div>
                        <div class="detail-value">${ticket.amount.toFixed(2)}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Due Date</div>
                        <div class="detail-value">{ticket.dueDate}</div>
                    </div>
                </div>
                <div class="button-group">
                    <button class="btn btn-secondary" on:click={() => viewDetails(ticket.id)}>
                        View Details
                    </button>
                    <button class="btn btn-primary" on:click={() => payTicket(ticket.id)}>
                        Pay Ticket
                    </button>
                </div>
            </div>
        {/each}
    </div>

    <div class="section">
        <h2 class="section-title">Payment History</h2>
        {#each paymentHistory as ticket}
            <div class="ticket-card">
                <div class="ticket-header">
                    <span class="ticket-id">{ticket.id}</span>
                    <span class="ticket-status status-{ticket.status.toLowerCase()}">{ticket.status}</span>
                </div>
                <div class="ticket-details">
                    <div class="detail-item">
                        <div class="detail-label">Type</div>
                        <div class="detail-value">{ticket.type}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Date</div>
                        <div class="detail-value">{ticket.date}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Amount</div>
                        <div class="detail-value">${ticket.amount.toFixed(2)}</div>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div> 