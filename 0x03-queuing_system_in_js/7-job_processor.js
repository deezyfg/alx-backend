#!/usr/bin/yarn dev
import kue from 'kue';

// Create a new queue
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];

/**
 * Sends a notification to a phone number with a given message.
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to be sent.
 * @param {Object} job - The Kue job object.
 * @param {function} done - The callback to be called when the job is complete.
 */
function sendNotification(phoneNumber, message, job, done) {
  let total = 2, pending = 2;
  let sendInterval = setInterval(() => {
    // Update job progress
    if (total - pending <= total / 2) {
      job.progress(total - pending, total);
    }

    // Check if the phone number is blacklisted
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }

    // Log the notification sending process
    if (total === pending) {
      console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
      );
    }

    // Complete the job when all pending operations are done
    --pending || done();
    pending || clearInterval(sendInterval);
  }, 1000);
}

// Define the queue name
const queueName = 'push_notification_code_2';

// Process jobs from the queue
queue.process(queueName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
