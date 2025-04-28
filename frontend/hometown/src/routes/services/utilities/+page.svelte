<script>
    let utilityAccounts = [
        {
            id: 'UTL-001',
            type: 'Water',
            currentBill: 85.50,
            dueDate: '2024-05-15',
            usage: {
                current: 1200,
                previous: 1100,
                unit: 'gallons'
            },
            status: 'Current'
        },
        {
            id: 'UTL-002',
            type: 'Electric',
            currentBill: 125.75,
            dueDate: '2024-05-15',
            usage: {
                current: 850,
                previous: 900,
                unit: 'kWh'
            },
            status: 'Current'
        }
    ];

    let paymentHistory = [
        {
            date: '2024-04-15',
            amount: 85.50,
            type: 'Water',
            status: 'Paid'
        },
        {
            date: '2024-04-15',
            amount: 125.75,
            type: 'Electric',
            status: 'Paid'
        }
    ];

    function payBill(accountId) {
        // Handle payment logic here
        console.log('Paying bill for account:', accountId);
    }

    function viewUsage(accountId) {
        // Handle view usage logic here
        console.log('Viewing usage for account:', accountId);
    }
</script>

<style>
    .utilities-container {
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

    .account-card {
        border: 1px solid #ececec;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .account-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .account-id {
        color: #2d2dff;
        font-weight: 600;
    }

    .account-status {
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }

    .status-current {
        background: #f0fff0;
        color: #43a047;
    }

    .status-past-due {
        background: #fff0f0;
        color: #e74c3c;
    }

    .usage-dashboard {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 1rem;
        padding: 1rem;
        background: #f8f9ff;
        border-radius: 8px;
    }

    .usage-item {
        text-align: center;
    }

    .usage-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d2dff;
    }

    .usage-label {
        color: #6c6c80;
        font-size: 0.9rem;
    }

    .bill-details {
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

<div class="utilities-container">
    <div class="section">
        <h2 class="section-title">Utility Accounts</h2>
        {#each utilityAccounts as account}
            <div class="account-card">
                <div class="account-header">
                    <span class="account-id">{account.id} - {account.type}</span>
                    <span class="account-status status-{account.status.toLowerCase().replace(' ', '-')}">
                        {account.status}
                    </span>
                </div>
                <div class="usage-dashboard">
                    <div class="usage-item">
                        <div class="usage-value">{account.usage.current}</div>
                        <div class="usage-label">Current Usage ({account.usage.unit})</div>
                    </div>
                    <div class="usage-item">
                        <div class="usage-value">{account.usage.previous}</div>
                        <div class="usage-label">Previous Usage ({account.usage.unit})</div>
                    </div>
                    <div class="usage-item">
                        <div class="usage-value">${account.currentBill.toFixed(2)}</div>
                        <div class="usage-label">Current Bill</div>
                    </div>
                </div>
                <div class="bill-details">
                    <div class="detail-item">
                        <div class="detail-label">Due Date</div>
                        <div class="detail-value">{account.dueDate}</div>
                    </div>
                </div>
                <div class="button-group">
                    <button class="btn btn-secondary" on:click={() => viewUsage(account.id)}>
                        View Usage History
                    </button>
                    <button class="btn btn-primary" on:click={() => payBill(account.id)}>
                        Pay Bill
                    </button>
                </div>
            </div>
        {/each}
    </div>

    <div class="section">
        <h2 class="section-title">Payment History</h2>
        {#each paymentHistory as payment}
            <div class="account-card">
                <div class="bill-details">
                    <div class="detail-item">
                        <div class="detail-label">Date</div>
                        <div class="detail-value">{payment.date}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Type</div>
                        <div class="detail-value">{payment.type}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Amount</div>
                        <div class="detail-value">${payment.amount.toFixed(2)}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Status</div>
                        <div class="detail-value">{payment.status}</div>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div> 