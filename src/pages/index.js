import React from "react"
import Layout from "../components/layout"
import SEO from "../components/seo"
import Apps from "../components/apps"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <div align={'center'}>
      <h1 style={{fontSize: '64px'}}>csmathtools</h1>
      <p style={{fontSize: '20px', marginBottom: '48px'}}>Calculators for Computer Science and Mathematics</p>
      <div style={{margin: '48px'}}>
        <Apps />
      </div>
    </div>
  </Layout>
)

export default IndexPage
