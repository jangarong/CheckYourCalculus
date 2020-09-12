import React from "react";
import { Link } from "gatsby";
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';

class Apps extends React.Component{
  constructor() {
    super();
    this.state = {
      width: 0,
      box_xs: 4
    };
  }
  // event listener for window size (to determine whether user is in mobile or not).
  componentDidMount() {
    this.handleWindowSizeChange()
    window.addEventListener('resize', this.handleWindowSizeChange);
  }
  componentWillUnmount() {
    window.removeEventListener('resize', this.handleWindowSizeChange);
  }
  handleWindowSizeChange = () => {
    this.setState({ width: window.innerWidth });
  };
  render() {
    const {width} = this.state;
    const isMobile = width <= 1280;
    if (isMobile){
      this.box_xs = 12;
    } else {
      this.box_xs = 4;
    }
    return (
      <Grid container spacing={3} justify={'space-evenly'}>
        <Grid item xs={this.box_xs}>
          <Paper style={{backgroundColor: '#3b3b3b', color: 'white', padding: '30px'}} elevation={4} align={'left'}>
            <h2>Compute</h2>
            <p>For every computational problem.</p>
            <div align={'right'}>
              <Link to={"/compute/"}>
                <Button color="secondary">Enter</Button>
              </Link>
            </div>
          </Paper>
        </Grid>
      </Grid>
    );
  }
}

export default Apps
