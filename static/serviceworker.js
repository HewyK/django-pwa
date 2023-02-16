var staticCacheName = 'pwa-test-v1' + new Date().getTime();

var filesToCache = [

];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("pwa-test-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
		// Prevent the default, and handle the request ourselves.
		event.respondWith((async () => {
		  // Try to get the response from a cache.
		  const cachedResponse = await caches.match(event.request);
		  // Return it if we found one.
		  if (cachedResponse) {
				//console.log('found in cache: ', event.request);
				return cachedResponse
			};
		  // If we didn't find a match in the cache, use the network.
		  //console.log('no cached item found, fetching from network: ', event.request);
		  return fetch(event.request);
		})());
	});

// Register event listener for the 'push' event.
self.addEventListener('push', (event) => {
    event.waitUntil(
      self.registration.showNotification('Notification Title', {
        body: 'Notification Body Text',
        icon: 'custom-notification-icon.png',
      })
    );
  });

// self.addEventListener('push', function (event) {
//     // Retrieve the textual payload from event.data (a PushMessageData object).
//     // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
//     // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
//     const eventInfo = event.data.text();
//     const data = JSON.parse(eventInfo);
//     const head = data.head || 'New Notification 🕺🕺';
//     const body = data.body || 'This is default content. Your notification didn\'t have one 🙄🙄';

//     // Keep the service worker alive until the notification is created.
//     event.waitUntil(
//         self.registration.showNotification(head, {
//             body: body,
//             icon: 'https://i.imgur.com/MZM3K5w.png'
//         })
//     );
// });