const BASE_URL = "http://127.0.0.1:5000";

// ---------------------------
// CREATE GROUP
// ---------------------------
async function createGroup() {
    let group_id = document.getElementById("group_id").value;
    let members = document.getElementById("members").value.split(",").map(m => m.trim());

    if (!group_id || members.length === 0) {
        alert("Please enter group ID and members!");
        return;
    }

    try {
        let res = await fetch(`${BASE_URL}/group/create`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ group_id, members })
        });

        let data = await res.json();

        if (res.ok) {
            alert("Group created successfully!");
            console.log("Response:", data);
        } else {
            alert("Error: " + (data.error || "Failed to create group"));
            console.error("Error response:", data);
        }
    } catch (error) {
        alert("Error: " + error.message);
        console.error("Fetch error:", error);
    }
}


// ---------------------------
// ADD MONEY
// ---------------------------
async function addMoney() {
    let name = document.getElementById("w_name").value;
    let group_id = document.getElementById("w_group").value;
    let amount = document.getElementById("w_amount").value;

    if (!name || !group_id || !amount) {
        alert("Please fill all fields!");
        return;
    }

    try {
        let res = await fetch(`${BASE_URL}/wallet/add`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, group_id, amount: parseFloat(amount) })
        });

        let data = await res.json();

        if (res.ok) {
            alert("Wallet updated!");
            console.log("Response:", data);
        } else {
            alert("Error: " + (data.error || "Failed to add money"));
            console.error("Error response:", data);
        }
    } catch (error) {
        alert("Error: " + error.message);
        console.error("Fetch error:", error);
    }
}


// ---------------------------
// GET SUMMARY
// ---------------------------
async function getSummary() {
    let group = document.getElementById("sum_group").value;

    if (!group) {
        alert("Please enter group ID!");
        return;
    }

    try {
        let res = await fetch(`${BASE_URL}/group/summary/${group}`);
        let data = await res.json();

        if (res.ok) {
            document.getElementById("summary_output").innerText =
                JSON.stringify(data, null, 4);
            console.log("Summary:", data);
        } else {
            alert("Error: " + (data.error || "Failed to get summary"));
            console.error("Error response:", data);
        }
    } catch (error) {
        alert("Error: " + error.message);
        console.error("Fetch error:", error);
    }
}


// ---------------------------
// ADD EXPENSE
// ---------------------------
async function addExpense() {
    let group_id = document.getElementById("e_group").value;
    let payer = document.getElementById("e_payer").value;
    let participants = document.getElementById("e_participants").value.split(",").map(m=>m.trim());
    let amount = document.getElementById("e_amount").value;
    let split_type = document.getElementById("e_split").value;

    if (!group_id || !payer || participants.length === 0 || !amount || !split_type) {
        alert("Please fill all fields!");
        return;
    }

    let payload = {
        group_id: parseInt(group_id),
        payer,
        participants,
        amount: parseFloat(amount),
        split_type
    };

    if (split_type === "ratio") {
        try {
            payload.ratio = JSON.parse(document.getElementById("e_ratio").value);
        } catch (e) {
            alert("Invalid ratio JSON format!");
            return;
        }
    }

    try {
        let res = await fetch(`${BASE_URL}/expense/split`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        let data = await res.json();

        if (res.ok) {
            alert("Expense added!");
            console.log("Response:", data);
        } else {
            alert("Error: " + (data.error || "Failed to add expense"));
            console.error("Error response:", data);
        }
    } catch (error) {
        alert("Error: " + error.message);
        console.error("Fetch error:", error);
    }
}
