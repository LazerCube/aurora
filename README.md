# This project is no longer being worked on and is being replaced by the Ceres project. [Ceres api][0] and [Ceres app][1]

# Aurora - Social network

Social networking website written in python using the Django framework.

## Dependencies

*   Django 1.9.2
*   Django Embed Video
*   Django Guardian
*   Pillow / PIL

## Features

*   Login and registration of new users.
*   User friendships. Includes requesting.
*   Realtime personal messaging system(Friends only atm)
*   User avatars
*   User activity feed. Both public and private activities.
*   News feed
*   Video posts. Youtube, Vimeo, SoundCloud currently supported.
*   Status update posts
*   Post comments.
*   Direct links to posts
*   Deletion of posts.
*   Basic user searching. Can search for and/or username, first name, last name.
*   UI written with mobile in mind.

## Changes with this version

*   Posting system - Basic posting system has been added. A user can now post status updates (text only) as well as video posts that can contain embedded media. Youtube, Vimeo, SoundCloud are currently the only media supported. Video posts are still a WIP and currently requires a user to paste the URL into a separate field in order to display the media as embedded content.

*   User avatars - Users now have a user avatar (profile icon) that will show next to their name on comments and posts. All icons are saved as 64 x 64 and are scaled down to this size.


## Coming soon™

*   Name
*   Liking system.
*   Posts direct views to be viewable without login.
*   Photo post.
*   Group chats.
*   Improved search.
*   Post, message and profile editing.
*   Replies for comments and messages.
*   New login page.
*   Better UI.
*   Alerts

## Improvements

*   Remove use of primary keys in URL
*   Update comments in real time
*   Pick out video url from status.
*   Custom video templates

## Current bugs:(

*   Sidebar doesn't close on some mobile devices.
*   Sidebar doesn't show active page.
*   New messages take too long to show for the sending user.
*   Current menu for posts doesn't work on mobile. (Needs replacing anyway)
*   Long comments go under the authors name in posts.


[0]: https://github.com/LazerCube/ceres_api
[1]: https://github.com/LazerCube/ceres_app
