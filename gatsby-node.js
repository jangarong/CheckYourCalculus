/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/node-apis/
 */

// used workaround in https://github.com/gatsbyjs/gatsby/issues/16112 to prevent
// 404 development page from showing up

exports.onCreatePage = ({ page, actions }) => {
  if (process.env.NODE_ENV !== `production` && page.path === `/404/`) {
    const { createPage } = actions
    // Make the 404 page match everything client side.
    // This will be used as fallback if more specific pages are not found
    page.matchPath = `/*`
    createPage(page)
  }
}