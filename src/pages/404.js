import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"

const NotFoundPage = () => (
  <Layout>
    <SEO title="404: Not found" />
    <div align={'center'}>
      <h1 style={{fontSize: '64px'}}>csmathtools</h1>
      <p style={{fontSize: '24px'}}>404: Not found</p>
    </div>
  </Layout>
)

export default NotFoundPage
