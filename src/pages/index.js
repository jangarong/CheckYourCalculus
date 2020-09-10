import React from "react"
import GitHubIcon from '@material-ui/icons/GitHub';
// import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <div align={'center'}>
      <h1 style={{fontSize: '64px'}}>csmathtools</h1>
      <p style={{fontSize: '24px'}}>Coming soon...</p>
      <p style={{fontSize: '18px', marginTop: '50px'}}>For now, why not check out our GitHub page?</p>
      <a href={'https://github.com/jangarong/csmathtools'}>
        <GitHubIcon style={{marginTop: '30px', width: '64px', height: '64px'}} />
      </a>
    </div>
  </Layout>
)

export default IndexPage
