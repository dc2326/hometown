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
    .voting-container {
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

    .info-card {
        border: 1px solid #ececec;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
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
        color: #6c6c80;
        font-size: 0.9rem;
    }

    .info-value {
        font-weight: 600;
        color: #2d2dff;
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .form-control {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #d1d5db;
        border-radius: 8px;
        font-size: 1rem;
    }

    .election-card {
        border: 1px solid #ececec;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .election-title {
        color: #2d2dff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .election-date {
        color: #7c3aed;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .election-description {
        color: #6c6c80;
        margin-bottom: 1rem;
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