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
    .fines-container {
        max-width: 800px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .section {
        background: white;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin-bottom: 2rem;
    }

    .section-title {
        color: #2d2dff;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }

    .ticket-card {
        border: 1px solid #ececec;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .ticket-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .ticket-id {
        color: #2d2dff;
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
        color: #43a047;
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
        color: #6c6c80;
        font-size: 0.9rem;
    }

    .detail-value {
        font-weight: 600;
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
    }

    .btn-primary {
        background: linear-gradient(90deg, #7c3aed, #2d2dff);
        color: white;
    }

    .btn-secondary {
        background: #f0f4ff;
        color: #2d2dff;
    }

    .btn:hover {
        opacity: 0.9;
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