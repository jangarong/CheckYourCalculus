// import React from "react"
// import { useState } from "react"
//
// export default function Compute() {
//   const [equation, isValid] = useState('');
//   return (
//     <div>
//       <blockquote>$\displaystyle{{ equation }}$</blockquote>
//         <form onClick={(e) => {
//           fetch('127.0.0.1:5000/api/eqs', {
//             method: 'POST',
//             body: JSON.stringify(e)
//           }).then(response => response.json()).then(data => {
//             this.setState({ equation: data['equation'] })
//               this.setState({ isValid: data['isValid'] })
//           })}}>
//           <input name={"text"} />
//           <input type={"submit"} />
//         </form>
//       <blockquote>${{ isValid }}$</blockquote>
//     </div>
//   )
// }
