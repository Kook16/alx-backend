import { expect } from 'chai';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
  let queue;
  let consoleSpy;

  beforeEach(() => {
    // Create a queue and enter test mode
    queue = kue.createQueue();
    kue.Job.rangeByType(
      'push_notification_code_3',
      'inactive',
      0,
      -1,
      'asc',
      function (err, jobs) {
        jobs.forEach(function (job) {
          job.remove();
        });
      }
    );
    queue.testMode.enter();
    consoleSpy = sinon.spy(console, 'log'); // Setup spy
  });

  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
    consoleSpy.restore(); // Restore spy
  });

  it('should display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create two new jobs to the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should log job status events', function (done) {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];

    // Simulate job events
    job.emit('enqueue');
    job.emit('complete');
    job.emit('failed', new Error('Failed to send notification'));
    job.emit('progress', 50);

    // Add individual checks to find out which assertion is failing
    try {
      sinon.assert.calledWith(
        consoleSpy,
        `Notification job created: ${job.id}`
      );
      sinon.assert.calledWith(
        consoleSpy,
        `Notification job ${job.id} completed`
      );
      sinon.assert.calledWith(
        consoleSpy,
        `Notification job ${job.id} failed: Error: Failed to send notification`
      );
      sinon.assert.calledWith(
        consoleSpy,
        `Notification job ${job.id} 50% complete`
      );
      done();
    } catch (error) {
      done(error); // Pass error to Mocha if an assertion fails
    }
  });
});
