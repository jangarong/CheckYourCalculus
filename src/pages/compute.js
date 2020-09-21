import React from "react"
import Layout from "../components/layout"
import SEO from "../components/seo"
import Compute from "../components/compute"

const ComputePage = () => (
  <Layout>
    <SEO title="Compute" />
    <div align={'center'}>
      <Compute />
    </div>
  </Layout>
)

export default ComputePage