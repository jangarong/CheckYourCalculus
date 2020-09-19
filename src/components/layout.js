import React from "react"

import Header from "./header"
import Footer from "./footer"
import '../styles/layout.css'

// issue with footer: won't stay down.

const Layout = ({ children }) => {

  return (
    <div style={{backgroundColor: '#2d2a2a'}}>
      <Header />
      <main style={{backgroundColor: '#2d2a2a', marginTop: '75px', marginBottom: '75px'}}>{children}</main>
      <Footer />
    </div>
  )
}


export default Layout