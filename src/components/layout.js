/**
 * Layout component that queries for data
 * with Gatsby's useStaticQuery component
 *
 * See: https://www.gatsbyjs.org/docs/use-static-query/
 */

import React from "react"

import Header from "./header"
import '../styles/layout.css'

const Layout = ({ children }) => {

  return (
    <div style={{backgroundColor: '#2d2a2a'}}>
      <Header />
        <main style={{backgroundColor: '#2d2a2a', marginTop: '75px', marginBottom: '75px'}}>{children}</main>
    </div>
  )
}


export default Layout
