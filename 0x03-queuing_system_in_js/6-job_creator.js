const kue = require('kue');
const queue = kue.createQueue();

// Object containing Job data
const jobData = {
    phoneNumber: "1234567890",
    message: "This is a notification message."
};

// Create a job
const job = queue.create('push_notification_code', jobData);

// Event handlers
job.on('complete', function() {
    console.log("Notification job completed");
});

job.on('failed', function() {
    console.log("Notification job failed");
});

// Save the job to the queue
job.save(function(err) {
    if (!err) {
        console.log("Notification job created:", job.id);
    } else {
        console.error("Error creating notification job:", err);
    }
});
