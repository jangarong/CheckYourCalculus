import React from "react"
import GitHubIcon from '@material-ui/icons/GitHub';
import '../styles/layout.css'

const Footer = () => (
  <div style={{backgroundColor: '#212121', padding: '30px'}} align={'center'}>
    <p>
      <a href={'https://github.com/jangarong/csmathtools'}>
        <GitHubIcon style={{width: '42px', height: '42px'}} />
      </a>
    </p>
    <p style={{color: '#777777'}}>Created by Jan Garong, Vivek Kandathil and Yining Wang.</p>
  </div>
)

export default Footer
