const form = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
form.addEventListener('submit', function (event) {
  event.preventDefault()
  const userId = event.target.dataset.userId
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken},
  })
    .then((response) => {
      console.log(response.data)
      const isFollowed = response.data.is_followed
      const followBtn = document.querySelector('#follow-form > input[type=submit]')
      if (isFollowed == true) {
        followBtn.value = '언팔로우'
      } else {
        followBtn.value = '팔로우'
      }
      
      const followerCountTag = document.querySelector('#followers-count')
      const followersCountData = response.data.followers_count
      followerCountTag.textContent = followersCountData
    })
})