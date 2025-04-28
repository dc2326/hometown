<script>
    let permits = [
        {
            title: 'Building Permit',
            description: 'Required for new construction, renovations, and major repairs',
            sampleUrl: '/permits/sample-building.pdf',
            applicationUrl: '/permits/apply-building',
            fee: '$150'
        },
        {
            title: 'Business License',
            description: 'Required for operating a business within town limits',
            sampleUrl: '/permits/sample-business.pdf',
            applicationUrl: '/permits/apply-business',
            fee: '$75'
        },
        {
            title: 'Special Event Permit',
            description: 'Required for public events, festivals, and large gatherings',
            sampleUrl: '/permits/sample-event.pdf',
            applicationUrl: '/permits/apply-event',
            fee: '$50'
        }
    ];

    function downloadSample(url) {
        window.open(url, '_blank');
    }

    function startApplication(url) {
        window.location.href = url;
    }
</script>

<style>
    .permits-container {
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

    .permit-card {
        border: 1px solid #ececec;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .permit-title {
        color: #2d2dff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .permit-description {
        color: #6c6c80;
        margin-bottom: 1rem;
    }

    .permit-fee {
        color: #7c3aed;
        font-weight: 600;
        margin-bottom: 1rem;
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

<div class="permits-container">
    <div class="section">
        <h2 class="section-title">Available Permits</h2>
        {#each permits as permit}
            <div class="permit-card">
                <h3 class="permit-title">{permit.title}</h3>
                <p class="permit-description">{permit.description}</p>
                <p class="permit-fee">Application Fee: {permit.fee}</p>
                <div class="button-group">
                    <button class="btn btn-secondary" on:click={() => downloadSample(permit.sampleUrl)}>
                        View Sample
                    </button>
                    <button class="btn btn-primary" on:click={() => startApplication(permit.applicationUrl)}>
                        Start Application
                    </button>
                </div>
            </div>
        {/each}
    </div>

    <div class="section">
        <h2 class="section-title">Application Status</h2>
        <p>Check the status of your permit applications or upload additional documents.</p>
        <button class="btn btn-primary" style="width: 100%;" on:click={() => window.location.href = '/permits/status'}>
            Check Application Status
        </button>
    </div>
</div> 