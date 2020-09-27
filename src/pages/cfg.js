import React from "react"
import Layout from "../components/layout"
import SEO from "../components/seo"
import CFG from "../components/cfg"

const CFGPage = () => (
  <Layout>
    <SEO title="CFGs" />
    <div align={'center'}>
      <CFG />
    </div>
  </Layout>
)

export default CFGPage