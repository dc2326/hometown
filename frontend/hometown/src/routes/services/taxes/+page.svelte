<script>
    let selectedForm = '';
    let taxYear = new Date().getFullYear();
    let questionnaireAnswers = {
        propertyOwned: false,
        businessOwned: false,
        incomeSource: '',
        deductions: []
    };

    function handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
            // Handle file upload logic here
            console.log('File uploaded:', file.name);
        }
    }

    function submitTaxes() {
        // Handle tax submission logic here
        console.log('Taxes submitted for year:', taxYear);
    }
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --primary-brown: #8b4513;
        --accent-gold: #d4af37;
        --background: #f5f5f0;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
    }

    .tax-container {
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

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 600;
        color: var(--primary-brown);
    }

    .form-control {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid rgba(139, 69, 19, 0.2);
        border-radius: 8px;
        font-size: 1rem;
        background: #fff;
        transition: border-color 0.3s;
    }

    .form-control:focus {
        outline: none;
        border-color: var(--primary-green);
    }

    .upload-area {
        border: 2px dashed rgba(139, 69, 19, 0.3);
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s;
        background: #fff;
    }

    .upload-area:hover {
        border-color: var(--primary-green);
        background: rgba(45, 90, 39, 0.02);
    }

    .checkbox-group {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }

    .checkbox-label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: var(--text-main);
    }

    .submit-btn {
        background: linear-gradient(90deg, var(--primary-green), var(--primary-brown));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        margin-top: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s;
    }

    .submit-btn:hover {
        background: linear-gradient(90deg, var(--primary-brown), var(--primary-green));
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(43, 43, 43, 0.2);
    }

    @media (max-width: 768px) {
        .checkbox-group {
            flex-direction: column;
        }
    }
</style>

<div class="tax-container">
    <div class="section">
        <h2 class="section-title">Tax Forms & Documents</h2>
        <div class="form-group">
            <label class="form-label">Select Tax Form</label>
            <select class="form-control" bind:value={selectedForm}>
                <option value="">Select a form</option>
                <option value="property">Property Tax Form</option>
                <option value="business">Business Tax Form</option>
                <option value="income">Income Tax Form</option>
            </select>
        </div>
        <div class="upload-area" on:click={() => document.getElementById('file-upload').click()}>
            <input type="file" id="file-upload" style="display: none" on:change={handleFileUpload} />
            <p>Click to upload your tax documents</p>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Supported formats: PDF, JPG, PNG</p>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">Tax Questionnaire</h2>
        <div class="form-group">
            <label class="form-label">Tax Year</label>
            <input type="number" class="form-control" bind:value={taxYear} />
        </div>
        <div class="checkbox-group">
            <label class="checkbox-label">
                <input type="checkbox" bind:checked={questionnaireAnswers.propertyOwned} />
                Do you own property?
            </label>
            <label class="checkbox-label">
                <input type="checkbox" bind:checked={questionnaireAnswers.businessOwned} />
                Do you own a business?
            </label>
        </div>
        <div class="form-group">
            <label class="form-label">Primary Income Source</label>
            <select class="form-control" bind:value={questionnaireAnswers.incomeSource}>
                <option value="">Select income source</option>
                <option value="employment">Employment</option>
                <option value="business">Business</option>
                <option value="investments">Investments</option>
                <option value="other">Other</option>
            </select>
        </div>
    </div>

    <button class="submit-btn" on:click={submitTaxes}>Submit Taxes</button>
</div> 