import http from 'k6/http';
import { sleep, check } from 'k6';
import { Counter } from 'k6/metrics';

// A simple counter for http requests

export const requests = new Counter('http_reqs');

// you can specify stages of your test (ramp up/down patterns) through the options object
// target is the number of VUs you are aiming for

/*
export const options = {
  stages: [
    { target: 20, duration: '1m' },
    { target: 15, duration: '1m' },
    { target: 0, duration: '1m' },
  ],
  thresholds: {
    requests: ['count < 100'],
  },
};
*/

let smoke_test = { 
    vus: 20, // 
    duration: `1m`
  
  };


let soak_test = {
  stages: [
    { duration: '5m', target: 500 }, // ramp up to 200 users
    { duration: '1h10m', target: 500 }, // stay at 200 for ~2 hours
    { duration: '2m', target: 0 }, // scale down. (optional)
  ],
};



export const options = smoke_test;

export default function () {
  // our HTTP request, note that we are saving the response to res, which can be accessed later

 
  

  const res2 = http.get('http://djangoapp-svc.architect.svc.cluster.local:8000/delay');

  

  const checkRes2 = check(res2, {
    'status is 200': (r) => r.status === 200
  });


  const res3 = http.get('http://djangoapp-svc.architect.svc.cluster.local:8000/random');

  

  const checkRes3 = check(res3, {
    'status is 200': (r) => r.status === 200
  });
}

