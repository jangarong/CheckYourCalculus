import React from "react"
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import '../styles/layout.css'

const Header = () => (
  <div>
    <AppBar style={{backgroundColor: '#3b3b3b'}} position="static">
      <Toolbar>
        <IconButton color="inherit" aria-label="menu">
          <MenuIcon />
        </IconButton>
      </Toolbar>
    </AppBar>
  </div>
)

export default Header
