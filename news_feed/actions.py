from django.contrib.contenttypes.models import ContentType
from models import Activity
from news_feed.signals import action

def action_handler(verb, **kwargs):
    kwargs.pop('signal', None)
    actor = kwargs.pop('sender')

    if hasattr(verb, '_proxy____args'):
        verb = verb._proxy____args[0]

    newaction = Activity.create(
        actor_content_type=ContentType.objects.get_for_model(actor),
        actor_object_id=actor.pk,
        verb=text_type(verb),
        public=bool(kwargs.pop('public', True)),
        description=kwargs.pop('description', None),
        timestamp=kwargs.pop('timestamp', now())
    )

    for opt in ('target', 'action_object'):
        obj = kwargs.pop(opt, None)
        if obj is not None:
            setattr(newaction, '%s_object_id' % opt, obj.pk)
            setattr(newaction, '%s_content_type' % opt,
                    ContentType.objects.get_for_model(obj))

    newaction.save()
    return newaction

action.connect(action_handler)
