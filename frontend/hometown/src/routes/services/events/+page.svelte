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

    .events-container {
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

    .event-card {
        border: 1px solid rgba(45, 90, 39, 0.1);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1rem;
        background: var(--card-bg);
        box-shadow: var(--card-shadow);
    }

    .event-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .event-title {
        color: var(--primary-green);
        font-weight: 600;
    }

    .event-date {
        color: var(--text-muted);
        font-size: 0.9rem;
    }

    .event-details {
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