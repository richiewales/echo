import React from 'react'
import PostItem from './post-item';

function PostContainer({ itemData }) {
  return (
    <section className="post-container">
      {itemData.map((post, index) => (
        <PostItem key={index} post={post} />
      ))}
    </section>
  )
}

export default PostContainer;
