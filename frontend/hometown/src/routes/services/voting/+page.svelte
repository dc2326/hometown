<script>
    let voterInfo = {
        registered: true,
        pollingLocation: '123 Community Center',
        precinct: 'Precinct 5',
        nextElection: '2024-11-05'
    };

    let ballotRequest = {
        electionDate: '',
        ballotType: 'mail',
        reason: ''
    };

    let elections = [
        {
            date: '2024-11-05',
            title: 'General Election',
            description: 'Vote for local officials and state representatives',
            registrationDeadline: '2024-10-15'
        },
        {
            date: '2024-08-15',
            title: 'Primary Election',
            description: 'Primary elections for state offices',
            registrationDeadline: '2024-07-25'
        }
    ];

    function requestBallot() {
        // Handle ballot request logic here
        console.log('Requesting ballot:', ballotRequest);
    }

    function checkRegistration() {
        // Handle registration check logic here
        console.log('Checking registration status');
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

    .voting-container {
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
        border: 1px solid rgba(139, 69, 19, 0.1);
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

    .info-card {
        border: 1px solid rgba(139, 69, 19, 0.1);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1rem;
        background: var(--card-bg);
        box-shadow: var(--card-shadow);
    }

    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }

    .info-item {
        margin-bottom: 1rem;
    }

    .info-label {
        color: var(--text-muted);
        font-size: 0.9rem;
    }

    .info-value {
        font-weight: 600;
        color: var(--primary-green);
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 600;
        color: var(--primary-green);
    }

    .form-control {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid rgba(45, 90, 39, 0.2);
        border-radius: 8px;
        font-size: 1rem;
        background: #fff;
        transition: border-color 0.3s;
    }

    .form-control:focus {
        outline: none;
        border-color: var(--primary-green);
    }

    .election-card {
        border: 1px solid rgba(139, 69, 19, 0.1);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1rem;
        background: var(--card-bg);
        box-shadow: var(--card-shadow);
    }

    .election-title {
        color: var(--primary-green);
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .election-date {
        color: var(--primary-green);
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .election-description {
        color: var(--text-muted);
        margin-bottom: 1rem;
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

<div class="voting-container">
    <div class="section">
        <h2 class="section-title">Voter Information</h2>
        <div class="info-card">
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-label">Registration Status</div>
                    <div class="info-value">{voterInfo.registered ? 'Registered' : 'Not Registered'}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Polling Location</div>
                    <div class="info-value">{voterInfo.pollingLocation}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Precinct</div>
                    <div class="info-value">{voterInfo.precinct}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Next Election</div>
                    <div class="info-value">{voterInfo.nextElection}</div>
                </div>
            </div>
            <button class="btn btn-secondary" on:click={checkRegistration} style="margin-top: 1rem;">
                Check Registration Status
            </button>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">Request a Ballot</h2>
        <div class="info-card">
            <div class="form-group">
                <label class="form-label">Election Date</label>
                <select class="form-control" bind:value={ballotRequest.electionDate}>
                    <option value="">Select an election</option>
                    {#each elections as election}
                        <option value={election.date}>{election.date} - {election.title}</option>
                    {/each}
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Ballot Type</label>
                <select class="form-control" bind:value={ballotRequest.ballotType}>
                    <option value="mail">Mail-in Ballot</option>
                    <option value="absentee">Absentee Ballot</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Reason for Request</label>
                <textarea class="form-control" bind:value={ballotRequest.reason} rows="3"></textarea>
            </div>
            <button class="btn btn-primary" on:click={requestBallot} style="width: 100%;">
                Request Ballot
            </button>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">Upcoming Elections</h2>
        {#each elections as election}
            <div class="election-card">
                <div class="election-title">{election.title}</div>
                <div class="election-date">Election Date: {election.date}</div>
                <div class="election-description">{election.description}</div>
                <div class="info-label">Registration Deadline: {election.registrationDeadline}</div>
            </div>
        {/each}
    </div>
</div> 