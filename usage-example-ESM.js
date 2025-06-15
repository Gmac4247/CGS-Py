// Insert this line into the legacy code to import specific functions from the module.

import { exactAreaOfCircle, exactCircumference, exactVolumeOfSphere, exactVolumeOfCone } from "./basic-geometry.mjs";

// Usage example of ES Module 
// Replacy legacy expressions by the exact ones where the output is. 

console.log(exactAreaOfCircle(r)); 
console.log(exactCircumference(r)); 
console.log(exactVolumeOfSphere(r)); 
console.log(exactVolumeOfCone(r, h));  
