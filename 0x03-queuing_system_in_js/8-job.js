#!/usr/bin/yarn dev
/**
 * Uses job array to create push Notification
 * @param {Job[]} jobs - Jobs in array
 * @param {Queue} queue - Order of jobs
 */

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error("Jobs is not an array");
    }

    jobs.forEach((jobData, index) => {
        const job = queue.create('push_notification_code_3', jobData);

        job.on('complete', function() {
            console.log("Notification job " + job.id + " completed");
        });

        job.on('failed', function(err) {
            console.log("Notification job " + job.id + " failed: " + err);
        });

        job.on('progress', function(progress) {
            console.log("Notification job " + job.id + " " + progress + "% complete");
        });

        job.save(function(err) {
            if (!err) {
                console.log("Notification job created: " + job.id);
            } else {
                console.error("Error creating notification job:", err);
            }
        });
    });
}

module.exports = createPushNotificationsJobs;
